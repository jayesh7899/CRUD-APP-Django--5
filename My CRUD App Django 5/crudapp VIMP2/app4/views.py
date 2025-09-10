from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Datas




# Create your views here.


def home(request):

    # for insert data
    data=Datas.objects.all()
    
    context={
        'data':data
    }

    return render(request,'index.html',context)


def adddata(request):
    # for insert data
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        obj=Datas()
        # also use below method for insert and update
        # obj=Datas(name=name, age=age, address=address, contact=contact, mail=mail)
        
        obj.name=name
        obj.age=age
        obj.address=address
        obj.contact=contact
        obj.mail=mail
        obj.save()
        return redirect('home')
    return render(request,'index.html')

# Delete data here
def deletedata(request,id):

    data=Datas.objects.get(id=id)
    data.delete()

    return redirect('/')

def updatedata(request,id):
    d1=Datas.objects.get(id=id)
    # for update data
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        
        # also use below method for insert and update
       
        d1.name=name
        d1.age=age
        d1.address=address
        d1.contact=contact
        d1.mail=mail
        d1.save()
        return redirect('home')
        

    return render(request,'update.html', {'dd':d1})

