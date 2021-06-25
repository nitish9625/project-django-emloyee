from django.shortcuts import render,HttpResponse,redirect
from employeeApp.forms import EmployeeForm
from employeeApp.models import Employee

# Create your views here.
def index(request):
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
        employee = Employee.objects.all()
    return render(request, "index.html",{'form':form, 'employees':employee})

def edit(request, id):
    employee = Employee.objects.get(id=id)  
    return render(request,'update.html',{'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'update.html', {'employee': employee})

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")    


