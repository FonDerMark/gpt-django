from django.db import models
from django.contrib.auth.models import User

class User_settings(models.Model):
    choises_mode = [
        ('you', 'you'), 
        ('poe', 'poe'),
        ('forefront', 'forefront'), 
        ('theb', 'thed') ,
    ]
    gpt_mode = models.CharField(max_length=20, choices=choises_mode, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.gpt_mode.capitalize()
    

class Telegram_user(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    extra_messages = models.IntegerField(null=True)
    day_limit_of_messages = models.IntegerField(null=True)
    day_of_limit = models.DateField(null=True)
    premium_status = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f'{self.username}({self.user_id})/limit:{self.day_limit_of_messages}'