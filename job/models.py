from django.db import models
# Create your models here.

class StudentUser(models.Model):
    fname = models.CharField(max_length=15, null=True)
    lname = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    pwd = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=15, null=True)
    contact = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)


class Recruiter(models.Model):
    finame = models.CharField(max_length=15, null=True)
    lname = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    pwd = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=15, null=True)
    contact = models.IntegerField( null=True)
    gender = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=20, null=True)





class Job(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    cname = models.TextField(null=True)
    image = models.FileField(null=True)
    title = models.CharField(max_length=100)
    salary = models.FloatField()
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()


class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()

class Admin(models.Model):
    uname = models.CharField(max_length=15, null=True)
    pwd = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=15, null=True)

class Feedback(models.Model):
    text = models.CharField(max_length=500,null=True)
