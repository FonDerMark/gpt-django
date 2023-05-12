from django.urls import path
from .views import Gpt, Api, Payment, gpt_mode

urlpatterns = [
    path('gpt_mode/', gpt_mode, name='gpt_mode'),
    path('', Gpt.as_view(), name='index'),
    path('api/payment/', Payment.as_view(), name='api'),
    path('api/', Api.as_view(), name='api'),
]