from django.shortcuts import render
from django.http import HttpResponse
from Students import views
# Create your views here.
def home(request,name):
	return HttpResponse("<h1>Welcome to APSSDC</h1>"+name+'<h1>Have a  good day</h1>')

def about(request,id):
	return HttpResponse("<h1>yes it is me {}</h1>".format(id))

def index(request):
	return render(request,'Students/index.html')

def hello(request,name,id):
	return HttpResponse("<h1>Welcome "+name+" ur roll no is {}</h1>".format(id))

def register(request):
	if request.method=='POST':
		emailId=request.POST['email']
		name=request.POST['name']
		#return HttpResponse("Suucessfully registered"+emailId)
		return render(request,'Students/success.html',{'name':name,'email':emailId})
	return render(request, 'Students/register.html')

def showdata(request):
	hero ={'name':'Mahesh','Age':44}
	return render(request,'Students/showdata.html',{'herodata':hero})