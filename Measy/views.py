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
    manager = get_object_or_404(Manager, cpf=id_manager)
    projectList = Project.objects.all()

    if request.method == "GET":
        print(id_manager)

    return render(request, "projects.html", {"manager": manager, "list": projectList})

def questions(request):

    return render(request, "questions.html")

def get_projects(request, id_project):
    projectList = Project.objects.all()

    return render(request, "projects.html", {"list": projectList})

def newProject(request, id_manager):
    manager = get_object_or_404(Manager, cpf=id_manager)

    if request.method == "POST":
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        manager = request.POST.get('manager', None)
        ty_pe = request.POST.get('type', None)
        methodology = request.POST.get('methodology', None)
        size = request.POST.get('size', None)

        print(type(name))

        objectManager = get_object_or_404(Manager, cpf=manager)
        # manager = Manager.objects.all()
        # man = Manager.objects
        # for i in list(manager):
        #     if (i.name == name):
        #         man = i

        project = Project(name=name, ty=ty_pe, size=size, methodology=methodology, manager=objectManager, description=description)
        project.save()
        return redirect('projects', objectManager.cpf)

    return render(request, "newProject.html", {"manager": manager})

def project(request, id_project):
    project = get_object_or_404(Project, id=id_project)

    return render(request, "project.html", {"project": project})