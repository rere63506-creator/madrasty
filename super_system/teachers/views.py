from django.shortcuts import render,redirect
from .models import Teacher,Student

def teacher_register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        Teacher.objects.create(name=name,phone=phone,password=password)
        return redirect('teacher_login')
    return render(request,'teacher_register.html')


def teacher_login(request):
    error=None
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        try:
            teacher=Teacher.objects.filter(name=name,password=password).first()
            request.session['teacher_id']=teacher.id
            return redirect('dashboard')
        except:
            error="please sure again from two feild"
    return render(request,'teacher_login.html',{'error':error})

def dashboard(request):
    teacher_id=request.session.get('teacher_id')
    if not teacher_id:
        return redirect('teacher_login')
    teacher=Teacher.objects.get(id=teacher_id)
    if request.method=='POST':
        name=request.POST.get('name')
        grade=request.POST.get('grade')
        phone=request.POST.get('phone')
        if name and grade:
            Student.objects.create(
                teacher=teacher,
                name=name,
                grade=grade,
                phone=phone,
            )
        return redirect('dashboard')
    all_student=Student.objects.filter(teacher=teacher)
    return render(request,'dashboard.html',{'students':all_student})

def student_login(request):
    error=None
    if request.method=='POST':
        name=request.POST.get('name')
        grade=request.POST.get('grade')
        try:
            student=Student.objects.filter(name=name,grade=grade).first()
            return redirect('student_detail',student_id=student.id)
        except student.DoesNotExist:
            error="the student is not found,please chick the name of student and the grade again"
    return render(request,'student_login.html',{'error':error})

def student_detail(request,student_id):
    student=Student.objects.get(id=student_id)
    return render(request,'student_detail.html',{'student':student})


def edit_student(request,student_id):
    student=Student.objects.get(id=student_id)
    if request.method=='POST':
        student.name=request.POST.get('name')
        student.grade=request.POST.get('grade')
        student.phone=request.POST.get('grade')
        student.attend=request.POST.get('attend')=='on'
        student.homework=request.POST.get('homework')=='on'
        student.paid=request.POST.get('paid')=='on'
        student.save()
        return redirect('dashboard')
    return render(request,'edit_student.html',{'student':student})


def delete_student(request,student_id):
    student=Student.objects.get(id=student_id)
    student.delete()
    return redirect('dashboard')
