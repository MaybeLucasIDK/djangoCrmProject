from django.shortcuts import render, redirect

from .forms import CreaterUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'webapp/index.html')


# register
def register(request):
    form = CreaterUserForm()
    
    if request.method == 'POST':
        form = CreaterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form': form}

    return render(request, 'webapp/register.html', context)



# login
def login(request):
    
    form = LoginForm()

    if request.method == "POST":
        
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            # checking if the user exists within the db
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form}

    return render(request, 'webapp/login.html', context=context)

# logout

def user_logout(request):
    auth.logout(request)
    return redirect('')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'webapp/dashboard.html')