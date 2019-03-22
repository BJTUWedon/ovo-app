
from django.shortcuts import render_to_response
from Admin import models
from django.shortcuts import HttpResponseRedirect

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def personal(request):
    return render_to_response('personal.html')

def admin(request):
    return render_to_response('admin.html')

def add_user(request):
    if request.method == "POST":

        name = request.POST.get("name", None)
        password = request.POST.get("password", None)
        age_choice = request.POST.get("age_choice", None)
        sex_choice = request.POST.get("sex_choice", None)
        character_choice = request.POST.get("character_choice", None)


        models.User.objects.create(
            name = name,
            password = password,
            age_choice = age_choice,
            sex_choice = sex_choice,
            character_choice = character_choice,

            )


        return HttpResponseRedirect(request,'Login.html')

@login_required(login_url='/Admin/login')
def home(request):
        return render(request, 'home.html', {'name': request.user.name})

def loginn(request):
        if request.method == 'GET':
            return render(request, 'login.html')
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')

        user = authenticate(name=name, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home.html'))
        else:
            return render(request, 'login.html',{'name': name, 'password': password, })
