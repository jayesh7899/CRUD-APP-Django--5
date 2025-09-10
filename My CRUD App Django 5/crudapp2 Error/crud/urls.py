from django.urls import path
from .views import*

urlpatterns = [
    
    path('home/',home),
    path('',stud_list,name="datalist"),
    path('create/',create,name="createdata"),
    path('update/<int:pk>/',update,name="updatedata"),
    path('delete/<int:pk>/',delete,name="deletedata"),



]
