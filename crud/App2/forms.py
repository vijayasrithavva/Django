from django.forms import ModelForm

from App2.models import Student

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'#['sudId','studName','branch','age']
		
			