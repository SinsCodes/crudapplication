from collections import defaultdict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import StudentRegistration
from .models import User

# Create your views here.
# this function is to add and show items
def add_show(request):

    if request.method == 'POST':

        fm = StudentRegistration(request.POST)

        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm= StudentRegistration()
            
    else:

        fm= StudentRegistration()

    stud=User.objects.all()

    return render(request,'enroll/addandshow.html',{'form':fm,'stud_info':stud})



#this function is to update items

def update_data(request,id):

    if request.method == 'POST':

        pi=User.objects.get(pk=id)

        fm=StudentRegistration(request.POST,instance=id)

        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            

    else:
        pi= User.objects.get(pk=id)

        fm=StudentRegistration(instance=id)

    return render(request,'enroll/updatestudent.html',{'form':fm})

#this function is to delete items
def delete_data(request, id):
    
     if request.method =='POST':

        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


    

