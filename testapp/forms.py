from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={
            'Id':forms.NumberInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Age':forms.TextInput(attrs={'class':'form-control'}),
            'Gender':forms.Select(attrs={'class':'form-control'}),
            'Mob_no':forms.NumberInput(attrs={'class':'form-control'}),
        }
