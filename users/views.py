from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout ,authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from . import forms
from . import models

class Register(CreateView):
    model = models.User
    form_class =  forms.RegisterCustomerForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
      
    def form_valid(self, form):
        form.instance.is_customer = True
        messages.success(self.request,'User made Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong, please try again later!')
        return super().form_invalid(form)  # Make sure to return the super's form_invalid

    
    
class Login(LoginView):
    template_name ='registration/login.html'   
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        messages.success(self.request,'You have successfully logged in!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Either the username or the password is wrong')
        return super().form_invalid(form)
    
class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request,'You have Logged out')
        return super().dispatch(request, *args, **kwargs)
    
