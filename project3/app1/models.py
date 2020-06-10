from django.db import models

# Create your models here.


class student(models.Model):
	roll_no = models.IntegerField()
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	username = models.CharField(max_length = 200)
	section = models.CharField(max_length = 5)
	branch = models.CharField(max_length = 20)
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200, default = "1234")
	status = models.CharField(max_length = 20, default = 'Active')
	phone_no = models.CharField(max_length = 20, default =" ")


	def __str__(self):
		return self.username






    
class teacher(models.Model):
	username = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	department = models.CharField(max_length = 20)
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)

	def __str__(self):
		return self.username





class query(models.Model):
	question=models.CharField(max_length = 400)
	date=models.DateTimeField(auto_now = True)
	student=models.OneToOneField(student , on_delete = models.CASCADE)
	answer=models.CharField(max_length = 400, default = "Query is not yet answered")
	queryStatus=models.CharField(max_length = 50, default = "Pending")
	subject=models.CharField(max_length = 50, default = "Query")



	def __str__(self):
		return self.question

	
