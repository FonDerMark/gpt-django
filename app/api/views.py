from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from os import environ as env
from django.core.serializers.json import DjangoJSONEncoder


from .request_to_gpt import request_to_gpt
from .models import Messages
from users.models import User_settings


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

    def get(self, request):
        return HttpResponse('ОК')
    
    def post(self, request):
        print(request.POST)
        user_id = request.POST['user_id']
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        question = request.POST['question']
        answer = request_to_gpt(question)
        data = {
            'user_id': user_id,
            'answer': answer,
        }
        try:
            return JsonResponse(data, encoder=MyJSONEncoder)
        except:
            return 'Null'
    

class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, str):
            return obj.encode('cp1251').decode('cp1251')
        return super().default(obj)
        