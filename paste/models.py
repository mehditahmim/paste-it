from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Paste(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    edited = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        url = reverse('paste:pasteView',[int(self.id)])
        return url 

