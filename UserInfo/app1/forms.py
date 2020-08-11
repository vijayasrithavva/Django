from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_info_form(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','password']#__all__'''