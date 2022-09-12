from email.policy import default
from tkinter import CASCADE
from turtle import color
from djongo import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
    # user_id = models.AutoField(primary_key=True)
    # email = models.EmailField(unique=True)
    
    # def __str__(self) :
    #     return str(self.user_id)

    # def __str__(self) -> str:
    #     return super().__str__(self.email)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True,null=False)
    book_name = models.CharField(max_length=200,unique=True)
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    book_author = models.CharField(max_length=40)

    def __str__(self):
        return self.name

