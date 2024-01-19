from django.contrib import admin

from  .models import Employee
class Employeeadmin(admin.ModelAdmin):
    list_display=('f_name','l_name','dept','salary','bonus','role','phone','hire_date')

admin.site.register(Employee,Employeeadmin)


from  .models import Role
class Roleadmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Role,Roleadmin)


from  .models import Department
class Departmentadmin(admin.ModelAdmin):
    list_display=('name','location')

admin.site.register(Department,Departmentadmin)

