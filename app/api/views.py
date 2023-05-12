from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from os import environ as env
from django.core.serializers.json import DjangoJSONEncoder
import datetime
import time


from .request_to_gpt import request_to_gpt
from .models import Messages
from users.models import User_settings, Telegram_user


@login_required
def gpt_mode(request):
    mode = request.GET['mode']
    user_id = request.user.id
    user, created = User_settings.objects.get_or_create(user_id=user_id)
    user.gpt_mode = mode
    user.save()
    return redirect('index')


class Gpt(View):

    def context(self, request, question=None):
        context = {}
        user_id = request.user.id
        context['messages'] = Messages.objects.filter(user_id=user_id)
        try:
            gpt_mode = User_settings.objects.get(user_id=user_id).gpt_mode
            context['gpt_mode'] = gpt_mode
        except:
            context['gpt_mode'] = env['GPT_MODE']
        if question:
            context['answer'] = request_to_gpt(question, context['gpt_mode'])
            Messages.objects.create(user_id=user_id, text=context['answer'])
        return context

    def get(self, request):
        return render(request, 'html/index.html', context=self.context(request))

    def post(self, request):
        question = request.POST['question']
        context = self.context(request, question)
        return render(request, 'html/index.html', context)
    

@method_decorator(csrf_exempt, name='dispatch')
class Api(View):
    
    # запрос в чат GPT
    def post(self, request):
        count_of_responses = 10
        user_id = request.POST['user_id']
        question = request.POST['question']
        user = self.get_or_create(request=request, user_id=user_id)
        if user.day_of_limit == datetime.date.today():
            if user.day_limit_of_messages > 0:
                answer = request_to_gpt(question)
                user.day_limit_of_messages -= 1
                user.save()
            elif user.extra_messages > 0:
                answer = request_to_gpt(question)
                user.extra_messages -= 1
                user.save()
            else:
                answer = 'Вы исчерпали лимит сообщений'
        else:
            answer = request_to_gpt(question)
            user.extra_messages = 9
            user.day_of_limit = datetime.date.today()
            user.save()
        print(answer)
        data = {
            'user_id': user_id,
            'answer': answer,
            'extra_messages': user.extra_messages,
            'day_limit_of_messages': user.day_limit_of_messages,
        }
        try:
            return JsonResponse(data, encoder=MyJSONEncoder)
        except:
            user.day_limit_of_messages += 1
            user.save()
        
    @staticmethod
    def get_or_create(request, user_id):
        user, created = Telegram_user.objects.get_or_create(user_id=user_id)
        if created:
            user.username = request.POST['username']
            user.firstname = request.POST['firstname']
            user.lastname = request.POST['lastname']
            user.extra_messages = 0
            user.day_limit_of_messages = 10
            user.day_of_limit = datetime.date.today()
            user.save()
        return user
    

class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, str):
            return obj.encode('cp1251').decode('cp1251')
        return super().default(obj)
        
@method_decorator(csrf_exempt, name='dispatch')
class Payment(View):

    def get(self, request):
        user = Api.get_or_create(request, request.GET['user_id'])
        data = {
            'extra_messages': user.extra_messages,
            'day_limit_of_messages': user.day_limit_of_messages,

        }
        return JsonResponse(data)

    def post(self, request, extra_messages=100):
        user_id = request.POST['user_id']
        user = Api.get_or_create(request=request, user_id=user_id)
        user.extra_messages += extra_messages
        user.save()
        return JsonResponse({
            'extra_messages': user.extra_messages,
            })
