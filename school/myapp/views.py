from pyexpat.errors import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . forms import Student, registerForm
from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from django.contrib.auth import login,logout


# Create your views here.
def index(request):
    return render(request,'index.html')
#crud
#c-create-add a record into db

def create_student(request):
    form=StudentForm( request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
      
    return render(request,'studentform.html',{'form':form})
    #fetching records from db
def read_student(request):
    students = Student.objects.all()
    return render(request,'admindashboard.html',{'students':students})
#u- update updates a record
def update_student(request,id):
    student = get_object_or_404(Student,pk=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request,'User created successfully')
        return redirect('students')
    return render(request,'studentform.html',{'form':form})
    #update
    #delite
def delete_student(request,id):
        student = get_object_or_404(Student,pk=id)
        student.delete()
        return redirect('students')
#create user
def register_user(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user')
    
    return render(request,'register.html',{'form':form})
def login_user(request):
    form = AuthenticationForm(request.POST or None)
    if form.is_valid():
       user= form.get_user()
       login(request,user)
       if user.is_staff:
           return redirect('user')
       return redirect('students')
    return render(request,'login.html' ,{'form':form})
def user_dashboard(request):
    return render(request,'admindashboard.html')
def logout_user(request):
    logout(request)
    return redirect('login')