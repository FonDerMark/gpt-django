from django.urls import path
from .views import Gpt, Api

urlpatterns = [
    path('', Gpt.as_view(), name='gpt'),
    path('api/', Api.as_view(), name='api')
]