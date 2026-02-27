from pyexpat.errors import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import Student
from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm


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
        messages.success(request,'student updated successfully')
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
    form = UserCreationForm()
    return render(request,'register.html',{'form':form})