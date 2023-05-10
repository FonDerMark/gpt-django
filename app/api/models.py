from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messages(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ['-datetime']