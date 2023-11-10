from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('home/', views.Home.as_view()),
    path('', views.Home.as_view()),
    path('addnote/', views.Add_note.as_view()),
    path('notes/', views.NotesV.as_view())


]
