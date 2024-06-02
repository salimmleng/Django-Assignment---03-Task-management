from django.shortcuts import render,redirect
from .forms import CategoryForm
# Create your views here.
def add_category(request):
    if request.method == "POST":
        category = CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            return redirect('add_category')
            

    else:
        category  = CategoryForm()

    return render(request,'category.html',{'form': category })