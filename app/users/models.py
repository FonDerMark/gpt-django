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