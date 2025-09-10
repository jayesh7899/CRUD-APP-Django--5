from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['stud_id','name','email','contact']

        widgets={
            'stud_id':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
        }