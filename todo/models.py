from tkinter import CASCADE
from turtle import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# this model is about features of to do list
class Todo(models.Model):
    # we need the user attribute 
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)

    # the title
    title = models.CharField(max_length=200)

    desc = models.TextField()

    pub_date = models.DateTimeField('date published', null=True, blank=True)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
