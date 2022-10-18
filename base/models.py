from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import false, null  

# Create your models here.

#Django has built in user models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    complete = models.BooleanField(default=false)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.title

    #Returns how we want to query the data, here we want the tasks which are not completed first
    class Meta:
        ordering = ['complete']
