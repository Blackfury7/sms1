from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from . models import teacher,student




def login(request):
	
	if request.method =="POST":
		print(request.body)
		
		data=json.loads(request.body)
		username=data["username"]
		password=data["password"]
		print(data)
		a=student.objects.filter(username=username,password=password,status="Active")
		b=teacher.objects.filter(username=username,password=password,status="Active")
		if a.exists():
			message = json.dumps({"id":a[0].id,
			"type":"student"})
		elif b.exists():
			message = json.dumps({"id":b[0].id,
			"type":"teacher"})
			
		else:
			message='{"type" : "invalid details"}'

		return JsonResponse(message,safe=False)


		


		
		


def teacherdashboard(request):
	
		
	if request.method =="GET":

		b=student.objects.filter(status = 'Active')		
		c=list(b.values())    
		
	return JsonResponse(c,safe=False)






   
            

		

	

