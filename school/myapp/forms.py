from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname','lastname','age','course']
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Age'}),
            'course':forms.Select(choices=[
                ('python','Python'),
                ('django','Django'),
                ('javascript','JavaScript'),
                ('react','React'),
                ('angular','Angular'),
                ('artificial intelligence','Artificial Intelligence')
            ]
            ,attrs={'class':'form-control'})
        }
class registerForm(UserCreationForm):
    class Meta:
       model=User
       fields=['username','email','first_name','last_name','password1','password2']
  
   
