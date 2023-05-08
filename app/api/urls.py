from django.urls import path

from .views import Gpt

urlpatterns = [
    path('', Gpt.as_view(), name='gpt'),
]