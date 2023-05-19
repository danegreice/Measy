from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Project, Manager
from .forms import ManagerForm
from django.contrib import messages

def login(request):
    if request.method == "POST":
        login = request.POST.get('username', None)
        password = request.POST.get('password', None)

        manager = Manager.objects.all()
        for i in list(manager):
            if ((i.login == login) and (i.password == password)):
                return redirect('home', i.cpf)
        messages.info(request, 'Usuário não encontrado')
        

    return render(request, "login.html")

def index(request):
            
    return render(request, "index.html")

def home(request, id_manager):
    manager = get_object_or_404(Manager, cpf=id_manager)
    print(manager.name)
    return render(request, "home.html", {"manager": manager})

def register(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        cpf = request.POST.get('cpf', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email', None)
        login = request.POST.get('login', None)
        password = request.POST.get('password', None)

        manager = Manager.objects.all()
        for i in list(manager):
            if (i.cpf == cpf):
                messages.info(request, 'Já cadastrado')

        manager = Manager(name=name, cpf= cpf, email= email, phone= phone, login= login, password= password)
        manager.save()
        return redirect('login')

        
    return render(request, "register.html")

def projects(request, id_manager):
    if request.method == "GET":
        print("oi")

    return render(request, "projects.html")

def get_projects(request, id_project):
    projectList = Project.objects.all()

    return render(request, "projects.html", {"list": projectList})

def newProject(request):

    return render(request, "newProject.html")

def project(request, id_project):
    project = get_object_or_404(Project, id=id_project)

    return render(request, "project.html", {"project": project})