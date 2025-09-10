from django.urls import path

from app4 import views


urlpatterns = [
  
    path('',views.home,name="home"),
    path('adddata',views.adddata, name="adddata"),
    path('deletedata/<int:id>',views.deletedata, name="delete"),
    path('updatedata/<int:id>',views.updatedata, name="updatedata"),
]
