from django.shortcuts import render
from django.views import View

from .request_to_gpt import request_to_gpt
from .models import Messages


class Gpt(View):

    def get(self, request):
        return render(request, 'html/index.html')
  
    def post(self, request):
        question = request.POST['question']
        answer = request_to_gpt(question)
        new_message = Messages()
        new_message.text = answer
        new_message.save()
        context = {
            'answer': answer,
        }
        return render(request, 'html/index.html', context=context)
    
    
class Api(View):

    def get(self, request):
        pass