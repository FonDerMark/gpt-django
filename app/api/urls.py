from django.urls import path
from .views import Gpt, Api, gpt_mode

urlpatterns = [
    path('gpt_mode/', gpt_mode, name='gpt_mode'),
    path('', Gpt.as_view(), name='index'),
    path('api/', Api.as_view(), name='api')
]