from django.shortcuts import render
from app1.forms import User_info_form

# Create your views here.
def register(req):
	form = User_info_form()
	return render(req,'app1/register.html',{'form':form})
