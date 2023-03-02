from . import views
from django.urls import path

urlpatterns = [

    path('', views.home,name='home'),
    path('signup', views.signup, name='signup'),
    path('saveuser', views.saveuser, name='saveuser'),
    path('logpage', views.logpage, name='logpage'),
    path('login', views.login, name='login'),
    path('otp', views.otp, name='otp'),
    path('resendotp', views.resendotp, name='resendotp'),
    path('football', views.football, name='football'),

]
