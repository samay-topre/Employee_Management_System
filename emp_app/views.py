from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Employee, Role, Department
from django.db.models import Q

def home(request):
    return render(request, 'index.html')

def viewall(request):
    viewlist = Employee.objects.all()
    context = {'x': viewlist}
    return render(request, 'viewall.html', context)

def remove(request):
    viewlist = Employee.objects.all()
    context = {'x': viewlist}
    return render(request, 'remove.html', context)

def removeindv(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return render(request, 'success.html')

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(f_name__icontains=name) | Q(l_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {'x': emps}
        return render(request, 'filtered.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')

def viewone(request, id):
    emp = get_object_or_404(Employee, id=id)
    context = {'x': emp}
    return render(request, 'viewone.html', context)

def add(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dept_id = request.POST.get('dept')
        phone = request.POST.get('phone')
        role_id = request.POST.get('role')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        hire = request.POST.get('hire')

        dept = Department.objects.get(pk=dept_id)
        role = Role.objects.get(pk=role_id)

        employee = Employee(f_name=fname, l_name=lname, dept=dept, phone=phone, role=role, salary=salary, bonus=bonus, hire_date=hire)
        employee.save()

    return render(request, 'add.html')
