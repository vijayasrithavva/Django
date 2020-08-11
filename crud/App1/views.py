from django.shortcuts import render,redirect
from django.http import HttpResponse
from App1.models import Emp
# Create your views here.
def signUp(request):
	if request.method == "POST":
		empId = request.POST['empId']
		empName = request.POST['empName']
		empDesig = request.POST['empDesig']
		salary = request.POST['salary']

		obj = Emp(empId=empId,empName=empName,empDesig=empDesig,salary=salary)
		obj.save()
		return redirect('/showall')
		#return HttpResponse('Done')
		#render showall.html at signup post method

	return render(request,'App1/signup.html')

def showAll(request):
	data = Emp.objects.all()
	return render(request,'App1/showall.html',{'data':data})
