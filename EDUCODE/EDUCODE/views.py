from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from backend.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def login_request(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('base')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            username = request.POST.get('email')
            password = request.POST.get('password')
            user_exists = User.objects.filter(email=username).exists()
            if user_exists:
                try:
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    print("You are now logged in as", username)
                    return redirect('index')
                except:
                    errors = "Incorrect Password"
                    print("Incorrect Password")
                    context['errors'] = errors
            else:
                print("username does not exists.")
                errors = "Username/Email does not exists."
                context['errors'] = errors
        form = AuthenticationForm()
        context['form'] = form
    return render(request, "Registration/login.html", context)



def logout_request(request):
    logout(request)
    print("Logged out successfully!")
    return redirect("/")



def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email are Already Exists !')
            return redirect('signup')

        # check username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username are Already exists !')
            return redirect('signup')
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        user = authenticate(username=email, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'Registration/signup.html')



def BASE(request):
    return render(request, 'base.html')


def INDEX(request):
    return render(request, 'index.html')


def ONE_COURSE(request):
    return render(request, '1course.html')


def ABOUT_US(request):
    return render(request, 'Pages/about_us.html')


def CONTACT_US(request):
    return render(request, 'Pages/contact_us.html')