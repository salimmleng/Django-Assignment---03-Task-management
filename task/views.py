from django.shortcuts import render,redirect
from task.forms import TaskForm
from task.models import TaskModel
# Create your views here.
def add_task(request):
    if request.method == "POST":
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('show_task')


    else:
        task = TaskForm()

    return render(request,'task.html',{'form': task})


def show_task(request):
    task = TaskModel.objects.all()
    return render(request,'show_task.html',{'tasks': task})

def edit_task(request,id):
    task1 = TaskModel.objects.get(pk = id)
    task = TaskForm(instance=task1)
    if request.method == "POST":
        task = TaskForm(request.POST,instance=task1)
        if task.is_valid():
            task.save()
            return redirect('show_task')
      
    return render(request,'edit_task.html',{'form': task})

def delete_task(request,id):
    task = TaskModel.objects.get(pk = id)
    task.delete()
    return redirect('show_task')