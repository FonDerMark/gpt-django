from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .request_to_gpt import request_to_gpt


class Gpt(View):

    def get(self, request):
        return render(request, 'html/test.html')
  
    def post(self, request):
        question = request.POST['question']
        response = request_to_gpt(question)
        context = {
            'answer': response,
        }
        return render(request, 'html/test.html', context=context)
    
    
class Api(View):

    def get(self, request):
        pass