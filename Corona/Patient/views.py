from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'Patient/home.html')

def register(request):
	return render(request,'Patient/register.html')

def login(request):
	if request.method=="POST":
		name = request.POST['name']
		password = request.POST['password']
		if name == "APSSDC" and password == "APSSDC":
			return HttpResponse('login successful')
		else:
			return HttpResponse('login unsuccessful')
	return render(request,'Patient/login.html')

def table(request,value):
	return render(request,'Patient/table.html',{'value':value})