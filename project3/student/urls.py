from django.urls import path

from . import views

urlpatterns = [
	path('studentDashboard/', views.studentDashboard, name='studentDashboard'),
	path('addStudent/', views.addStudent, name='addStudent'),
	path('updateStudent/', views.updateStudent, name='updateStudent'),
	path('deleteStudent/', views.deleteStudent, name='deleteStudent'),
	
	path('addQuery/', views.addQuery, name='addQuery'),
	path('updateQuery/', views.updateQuery, name='updateQuery'),
	path('queryDetail/', views.queryDetail, name='queryDetail'),
	path('queryList/', views.queryList, name='queryList'),
	path('addQueryAnswer/', views.addQueryAnswer, name='addQueryAnswer'),

	
	
]