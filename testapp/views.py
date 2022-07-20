from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from testapp.models import Student
from testapp.forms import StudentForm
# Create your views here.
def home(request):
    return HttpResponse('hello')

def student(request):
    records=Student.objects.all()
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    context={
        'records':records,'form':form
    }
    return render(request,'testapp/student.html',context)