from django.shortcuts import render
from django.http import HttpResponse
from App2.models import Mobiles
from App2.models import Library
# Create your views here.

def mobiles(request):
	if request.method=='POST':
		Model = request.POST['model']
		Cost = request.POST['cost']
		Year = request.POST['year']
		obj = Mobiles(model=Model,cost=Cost,year=Year)
		obj.save()
		return HttpResponse("DOne ")
		#return render(request, 'display.html', {'Model':Model,"Cost":Cost,"Year":Year})
	return render(request,'data.html')
def library(request):
	if request.method=='POST':
		BookName = request.POST['bookName']
		Department = request.POST['department']
		Author = request.POST['author']
		Year = request.POST['year']
		obj = Library(bookName=BookName,department=Department,author=Author,year=Year)
		obj.save()
		data = Library.objects.all()
		context = {'data':data}
		return render(request,'displaybooks.html',context)
		#return render(request,'displaybooks.html',{'BookName':BookName,'Department':Department,'Author':Author,'Year':Year})
	return render(request,'bookdetails.html')
	'''data = Library.objects.all()
	context = {'data':data}
	return render(request,'displaybooks.html',context)'''
	