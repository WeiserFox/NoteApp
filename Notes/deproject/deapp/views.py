from django.shortcuts import render
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from . import models

class Register(View):
    def get(self, request):
        return render(request, 'reg.html')
    def post(self, request):
        data = request.POST
        user_name = data['username']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password1']
        check_password = data['password2']
        if password == check_password:
            user = models.User()
            user.create_user(user_name, first_name, last_name, email, password)
            return render(request, 'redirect.html')
        else:
            return HttpResponse("Пароли не совпадают!")


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        data = request.POST
        username = data['username']
        try:
            user = authenticate(request, username=username, password=data['password'])
            if user is None:
                return HttpResponse("Неправильное имя пользователя или пароль")
            login(request, user)
            return render(request, "redirect.html")
        except KeyError:
            return HttpResponse("<h3>Заполните все поля</h3>")

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponse("Вы вышли из аккаунта")

class Add_note(View):
    def get(self, request):
        return render(request, 'addnote.html')
    def post(self, request):
        data = request.POST
        title = data['title']
        text = data['text']
        note = models.Notes()
        note.create_note(request.user.username, title, text)
        return HttpResponse("Заметка добавлена")

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {'first_name': request.user.first_name}
            return render(request, 'home.html', context)
        else:
            context = {'first_name': "Аноним"}
            return render(request, 'home.html', context)

class NotesV(View):
    def get(self, request):
        notes = models.Notes.objects.filter(author=request.user.username)
        for note in notes:
            print(note.text)
        print(notes)
        context = {'notes': notes}
        return render(request, 'notes.html', context)

