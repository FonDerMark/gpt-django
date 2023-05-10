from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User

from .request_to_gpt import request_to_gpt
from .models import Messages


class Gpt(View):

    def get(self, request):
        messages = Messages.objects.filter(user_id=request.user.id)[0:10]
        context = {
            'messages': messages,
        }
        return render(request, 'html/index.html', context=context)
  
    def post(self, request):
        question = request.POST['question']
        answer = request_to_gpt(question)
        user = request.user
        new_message = Messages(text=answer, user=User.objects.get(id=user.id))
        new_message.save()
        messages = Messages.objects.filter(user_id=request.user.id)[1:11]
        context = {
            'answer': answer,
            'messages': messages,
        }
        return render(request, 'html/index.html', context=context)
    
    
class Api(View):

    def get(self, request):
        pass