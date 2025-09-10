from django.shortcuts import render,redirect, get_object_or_404
from .models import Student

# Create your views here.
def index(request):
    
    data=Student.objects.all()
    print(data)
    context={'data':data}
    return render(request,'index.html', context)

def insertdata(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email, age, gender)
        query=Student(name=name,email=email, age=age,gender=gender)
        query.save()
        return redirect('/')
    return render(request,'index.html')

def updatedata(request,id):
    d=get_object_or_404(Student, id=id)
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        d.name=name
        d.email=email
        d.age=age
        d.gender=gender
        d.save()

        return redirect('/')

    
    context={'d':d}

    return render(request,'update.html', context)
    
def deletedata(request,id):
    
    data=Student.objects.get(id=id)
    data.delete()
    
    return redirect('/')