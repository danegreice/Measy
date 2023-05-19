from django.urls import path, include

from .views import login, index, get_projects, project, register, home, projects, newProject

urlpatterns = [
    path('', index, name="index"),
    path('', include('django.contrib.auth.urls')),
    path('login', login, name="login"),
    path('project/<int:id_project>', project, name="project"),
    path('register', register, name="register"),
    path('projects/<str:id_manager>', projects, name="projects"),
    path('newProject', newProject, name="newProject"),
    path('home/<str:id_manager>', home, name="home")
]