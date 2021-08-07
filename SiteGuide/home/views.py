from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Patient
from .forms import PatientForm


# Create your views here.
def index(request):
    data = Patient.objects.all()
    return render(request, 'index.html', {'all_data': data})


def add_user(request):
    if request.method == 'POST':
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PatientForm()
    return render(request, 'add.html', {'form': form})
def edit_Patient(request,id):
    if request.method=='POST':
        data=Patient.objects.get(pk=id)
        form=PatientForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        data = Patient.objects.get(pk=id)
        form = PatientForm(instance=data)
    return render(request,'update.html',{'form':form})
def delete(request,id):
    if request.method=='POST':
        pt=Patient.objects.get(pk=id)
        pt.delete()
    return HttpResponseRedirect('/')