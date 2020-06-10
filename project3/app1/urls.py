from django.urls import path

from . import views

urlpatterns = [
	path('', views.login, name='login'),
	path('teacherdashboard/', views.teacherdashboard, name='teacher'),
	# path('student/', views.teacher, name='student'),
	# path('add_student/', views.teacher, name='add_student'),
	# path('update/', views.teacher, name='update'),
	# path('delete/', views.teacher, name='delete'),
	# path('raisequery/', views.teacher, name='raisequery'),
    
    
    

]