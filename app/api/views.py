from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from gpt4free import Provider, quora, forefront
import gpt4free

class Gpt(View):

    def get(self, request):
        return render(request, 'html/test.html')
    
    # def post(self, request):
    #     question = request.POST['question']
    #     response = gpt4free.Completion.create(Provider.You, prompt=question)
    #     return HttpResponse(response)

    def post(self, request):
        question = request.POST['question']
        response = gpt4free.Completion.create(Provider.Theb, prompt=question)
        context = {
            'answer': response,
        }
        return render(request, 'html/test.html', context=context)
    
class Api(View):

    def get(self, request):