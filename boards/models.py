from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.CharField(max_length=150)

class Topic(models.Model):
    subject=models.CharField(max_length=250)
    board=models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)

