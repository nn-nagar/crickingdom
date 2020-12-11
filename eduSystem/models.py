from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name="Name")
    subjects  = models.ManyToManyField(Subject,related_name='teacher_subject')

    def __str__(self):
        return self.name

class Student(models.Model):
    student_name = models.CharField(max_length=100, null=True ,blank=True, verbose_name="Student_name")
    username = models.OneToOneField(User,on_delete=models.CASCADE, null=True, verbose_name="User")
    Teachers = models.ManyToManyField(Teacher,blank=True,related_name='student_teacher',verbose_name="student_teacher")

    def __str__(self):
        return self.student_name

    def get_teachers(self):
        return ",".join([str(p) for p in self.Teachers.all()])


    

