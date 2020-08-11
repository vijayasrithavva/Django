from django.shortcuts import render
from App.forms import MyForm 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(req):
	if req.method == 'POST':
		data=MyForm(req.POST)
		if data.is_valid():
			data.save()
			return HttpResponse('<h1>Registration Successfull</h1>')
	form = MyForm()
	return render(req,'register.html',{'form':form})

def home(req):
	return render(req,'home.html')
	
@login_required
def profile(req):
	data = User.objects.all()
	return render(req,'profile.html',{'data':data})

