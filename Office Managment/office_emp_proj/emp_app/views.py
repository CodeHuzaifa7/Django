from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])

        new_value = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_value.save()
        return  HttpResponse("Employee added Successful")
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return  HttpResponse("An Error Occured! Details has not been submitted")

def remove_emp(request ,emp_id=0):
    if (emp_id!=0):
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed sucessfully")
        except:
            return HttpResponse("Please enter a valid Empid")
    emps= Employee.objects.all()
    context = {'emps': emps}
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(first_name__icontains = name))
        if dept:
            emps = emps.filter(Q(dept__name__icontains= dept))
        if role:
            emps = emps.filter(Q(role__name__icontains = role))


        context ={
            'emps' : emps
        }
        return render(request,'all_emp.html',context)


    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse("An Error Occured! Details has not found")