from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from App2.forms import StudentForm
from App2.models import Student

# Create your views here.
def hello(request):
	return HttpResponse('From App2')

def register(request):
	#form = StudentForm()
	if request.method == "POST":
		form=StudentForm(request.POST)
		#for messages
		if form.is_valid():
			form.save()
			messages.success(request,request.POST['studName']+'record is added successfully')
		
		return redirect('/app2/register')
		#return HttpResponse("DONE")
	form = StudentForm()
	return render(request,'App2/register.html',{'form':form})

def details(request):
	data = Student.objects.all()
	return render(request,'App2/details.html',{'data':data})

def edit(request,id):
	data = Student.objects.get(id=id)
	if request.method=="POST":
		form= StudentForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/app2/details')
	form = StudentForm(instance=data)
	return render(request,'App2/edit.html',{'form':form,'data':data})

def delete(request,id):
	ob = Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/app2/details')
	return render(request,'App2/msg.html',{'info':ob})

