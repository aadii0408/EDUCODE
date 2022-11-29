"""EDUCODE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from . import views, user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base',views.BASE,name='base'),
    path('',views.INDEX,name='index'),

    path('login_page/', views.login_request, name = 'login_page'),
    path('logout_request/', views.logout_request, name = 'logout_request'),

    path('user_signup/', views.user_signup, name='user_signup'),






    path('1/course',views.ONE_COURSE,name='1course'),
    path('about',views.ABOUT_US,name='about_us'),
    path('contact',views.CONTACT_US,name='contact_us'),

    # path('Registration/signup', user_login.SIGN_UP, name='signup'),
    # path('Registration/', include('django.contrib.auth.urls')),

    # path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('Registration/profile', user_login.PROFILE, name='profile'),
    path('Registration/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),

]
