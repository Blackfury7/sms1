from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from . models import teacher,student




def login(request):
	
	if request.method =="POST":
		# print(request.body)
		body=request.body.decode('utf-8')
		data=json.loads(body)
		username=data["username"]
		password=data["password"]

		a=student.objects.filter(username=username).filter(status="Active")
		b=teacher.objects.filter(username=username)
		print(data)

		message = "wrong username"
		if a.count()==1:
			print(a)
			if a.filter(password=password).count()==1:
				message = "Wellcome Student"
			else:
				message = "wrong password"


		if b.count()==1:
			if b.filter(password=password).count()==1:
				message = "Wellcome Teacher"
			else:
				message = "wrong password"



		
		return JsonResponse(message,safe=False)


		


		
		


def teacherdashboard(request):
	
		
	if request.method =="GET":

		b=student.objects.filter(status = 'Active')		
		c=list(b.values())    
		
	return JsonResponse(c,safe=False)






   
            

		

	

