from django.urls import path
from App2 import views

urlpatterns = [
	path('',views.hello,name='hello'),
	path('register/',views.register,name='register'),
	path('details/',views.details,name='details'),
	path('edit/<int:id>',views.edit,name='edit'),
	path('delete/<int:id>',views.delete,name='delete'),#dynamic url mapping (<int:id>)


]