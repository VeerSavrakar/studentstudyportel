from django import forms
from dashboard.models import Notes,HomeWork,Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
class Noteform(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']
        
        
class DateInput(forms.DateInput):
    input_type = 'date'
class HomeworkForm(forms.ModelForm):
    class Meta:
        model=HomeWork
        fields=['subject','title','description','due','is_finished']
        widgets = {
            'due': DateInput()  # Properly applying the DateInput widget to the 'due' field
        }

class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search")
    
class Todoform(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']
        
class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
        