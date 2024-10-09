from django.contrib.auth.forms import UserCreationForm
from . import models

class RegisterCustomerForm(UserCreationForm):
    
    class Meta:
        model = models.User
        fields = ['username', 'email','password1','password2']
    