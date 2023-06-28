from django.urls import path, include

from .views import login, index, get_projects, project, register, home, projects, newProject, questions

urlpatterns = [
    path('', index, name="index"),
    path('', include('django.contrib.auth.urls')),
    path('login', login, name="login"),
    path('project/<int:id_project>', project, name="project"),
    path('register', register, name="register"),
    path('questions/<int:id_project>', questions, name="questions"),
    path('projects/<str:id_manager>', projects, name="projects"),
    path('newProject/<str:id_manager>', newProject, name="newProject"),
    path('home/<str:id_manager>', home, name="home")
]