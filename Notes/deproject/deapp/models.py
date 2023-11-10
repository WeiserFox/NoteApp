from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # Модель пользователя
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField
    password = models.CharField(max_length=15)
    def create_user(self, user_name, first_name, last_name, email, password): #  Метод создаёт пользователя в БД
        self.username = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.save()

class Notes(models.Model): # Модель заметок
    author = models.CharField(default='noname', max_length=10)
    title = models.CharField(max_length=10)
    text = models.CharField(max_length=250, default='Nothing')
    def create_note(self, author, title, text):  # Метод создаёт заметку в БД
        self.author = author
        self.title = title
        self.text = text
        self.save()

