from django.contrib import admin
from employeeApp.models import Employee

# Register your models here.
class EmployeeList(admin.ModelAdmin):
    list_display=['empcode','empname','empemail']


admin.site.register(Employee, EmployeeList)
