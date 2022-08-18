from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            reg = User(name=nm, email=pw, password=pw)
            reg.save()
            form= StudentRegistration() #later for success or redirect
    else:
        form = StudentRegistration()
        
    stud = User.objects.all()
    
    return render(request, 'enroll/addandshow.html', {'form':form,'stu':stud})

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':form})