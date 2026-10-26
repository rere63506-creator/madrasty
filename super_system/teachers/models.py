from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    grade=models.CharField(max_length=50,null=True,blank=True)
    attend=models.BooleanField(default=True)
    homework=models.BooleanField(default=False)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    done=models.BooleanField(default=False)


class Homework(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='homework_list')
    date=models.DateField(auto_now_add=True)
    done=models.BooleanField(default=False)
    note=models.CharField(max_length=20,blank=True)


class Payment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    paid=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.student.name}-{self.date}"