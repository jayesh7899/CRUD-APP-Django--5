from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student



# Create your views here.
def home(request):

    return HttpResponse("Hello")

def create(request):

    if request.method=='POST':
        form=StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('createdata')
        form=StudentForm()
        
    else:
        form=StudentForm()
       

    return render(request,'create.html',{'form':form})


#list view

def stud_list(request):
    student=Student.objects.all()

    return render(request,'list.html',{'student':student})


#update view    

def update(request,pk):
    studupdate=Student.objects.all()
    print(studupdate)
  
    try:
        if request.method=='POST':

            studupdate=Student.objects.get(id=pk)

            
            form=StudentForm(request.POST,instance=studupdate)


            if form.is_valid():
                form.save()
                return redirect('datalist')
    
        else:
            form=StudentForm(instance=Student)

    except Exception as e1:
        print('err', e1)
    
    return render(request,'update.html', {'form':form, 'pk':pk})



#delete view

def delete(request,pk):
    
    if request.method=="POST":
        deletestud=Student.objects.get(id=pk)
        deletestud.delete()
    return redirect('datalist')

