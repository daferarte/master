from django.shortcuts import render, redirect
from .models import Personas
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    try:
        usuario=User.objects.get(pk=request.user.id)
        persona=Personas.objects.get(user=usuario)
    except User.DoesNotExist:
        persona=Personas.objects.get(pk=1)

    return render(request, 'mainapp/index.html',{
        'title': 'Investigación',
        'persona':persona,
    })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == 'POST':
            username=request.POST.get('usuario')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)
            if( user is not None):
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'Usuario o contraseña incorrectos')

        return render(request, 'mainapp/login.html',{
            'title': 'Login',
        })

def logout_user(request):
    logout(request)
    return redirect('index')

# metodo que requeriere no estar inicido sesion para guardar
# def register_page(request):

#     if request.user.is_authenticated:
#         return redirect('index')
#     else:
#         register_form = RegisterForm()

#         if request.method == 'POST':
#             register_form=RegisterForm(request.POST)

#             if(register_form.is_valid()):
#                 register_form.save()
#                 messages.success(request,'Registro exitoso')
#                 return redirect('index')
        
#         return render(request, 'mainapp/register.html',{
#             'title': 'Crear usuario',
#             'register_form':register_form
#         })

@login_required(login_url='login')
def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form=RegisterForm(request.POST)

        if(register_form.is_valid()):
            register_form.save()
            messages.success(request,'Registro exitoso')
            return redirect('index')
    
    return render(request, 'mainapp/register.html',{
        'title': 'Crear usuario',
        'register_form':register_form
    })