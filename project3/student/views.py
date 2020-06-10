from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from app1 . models import teacher,student,query
from django.db.models import F
import datetime





def studentDashboard(request):
	if(request.method == "POST"):
		body=request.body.decode('utf-8')
		data=json.loads(body)
		print(data)
		username=data["username"]

		a=student.objects.filter(username=username)
		b=list(a.values())
		print(b)


		c=query.objects.filter(student__username = username)
		print(c.values())
		if c.count()==1:
			b.append(list(c.values()))


	return JsonResponse(b,safe=False)



def addStudent(request):
	if(request.method == "POST"):


		body=request.body.decode('utf-8')
		print('booooodyyyy',body)
		data=json.loads(body)

		print('daaataaaaa',data)

		
		first_name=data['first_name']
		last_name=data['last_name']
		section=data['section']
		branch=data['branch']
		email=data['email']
		phone_no=data['phone_no']

		def checkEmail(email):
				if email.endswith("@gmail.com") and email.len()>9:
					return (True)
				else:
					return (False)	

		
		if first_name!=None and branch!=None and section!=None and len(phone_no)==10 and checkEmail(email):
			x=student.objects.last()
			y=student.objects.filter(status = 'Active').last()
			
			user=str(first_name)
			uid=str(x.pk+1)

			roll_no=y.roll_no+1
			username="S."+user+"."+uid

			a=student(roll_no=roll_no,first_name=first_name,last_name=last_name,username=username,section=section,branch=branch,email=email,phone_no=phone_no)
			a.save()
			message="Student Added Successfully"

		else:
			message="Invalid details"



	return JsonResponse(message,safe=False)




def updateStudent(request):
	if(request.method == "POST"):
		body=request.body.decode('utf-8')
		data=json.loads(body)

		id=int(data['id'])

		
		username="S."+data['first_name']+"."+data['id']
		
		print('dataa',data)
		
		a=student.objects.filter(pk=id)
		print(a.count())
		print("a",a)
		a.update(username=username,**data)
		print(a)
		
		
		message="Student data updated successfully"
	
	
	return JsonResponse(message,safe=False)


def deleteStudent(request):
	if(request.method == "POST"):
		body=request.body.decode('utf-8')
		data=json.loads(body)

		id=int(data['id'])

		
		
		
	
		
		a=student.objects.filter(pk=id)
		print(a.count())
		
		a.update(status="Inactive")

		b=student.objects.filter(pk__gt = id).filter(status="Active")
		if b.count()>0:
			b.update(roll_no = F('roll_no') - 1)
		
		
		message="Student data deleted"
	
	
	return JsonResponse(message,safe=False)



def addQuery(request):
	if(request.method == "POST"):
		body=request.body.decode('utf-8')
		data=json.loads(body)

	
		username=data['username']

		question=data['question']
		subject=data['subject']
		
		pk=student.objects.get(username=username).pk
		if query.objects.filter(student_id=pk).count()!=0:
			return JsonResponse("Query is already raised. You can update your query in Update Query.",safe=False)

		a=query.objects.create(student_id=pk , subject = subject , question = question)
		
		
		return JsonResponse("Query is sent",safe=False)

def updateQuery(request):
	if(request.method == "POST"):
		body=request.body.decode('utf-8')
		data=json.loads(body)

	
		username=data['username']

		question=data['question']
		subject=data['subject']
		x = datetime.datetime.now()
		
		
		a=query.objects.filter(student__username = username)
		print(a)
		if a.count()==1:
			a=a.update(subject = subject , question = question , date = x)
			message="Query is updated"
		else:
			message = "Query is not created. Create Query first."
		
		
		
		return JsonResponse(message,safe=False)



def addQueryAnswer(request):
	if(request.method == "POST"):
		body=request.body.decode('utf-8')
		data=json.loads(body)

		pk=int(data['pk'])
		answer = data['answer']

		a=query.objects.filter(student_id = pk)
		a=a.update( answer = answer, queryStatus = "Answered")


		return JsonResponse(a,safe=False)
		
		






def queryList(request):
	
	if(request.method == "GET"):
		a=query.objects.filter(queryStatus="Pending").order_by('student_id')
		print(a)
		a=list(a.values())
		b=student.objects.filter(query__queryStatus = "Pending").filter(status="Active")
		print(b)
		b=list(b.values())
		b=b+a
	
		
	
	return JsonResponse(b,safe=False)



def queryDetail(request):
	if(request.method == "POST"):
		body=request.body.decode('utf-8')
		data=json.loads(body)

		id=int(data['pk'])

		a=query.objects.filter(student_id=id)

		a=list(a.values())

	return JsonResponse(a,safe=False)

				



		
		
		
	
		
		



		


		




			



