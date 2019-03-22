from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category


def index(request):
    return render(request, 'category/index.html')


def addCategory(request):
    if request.method == 'POST':
        name = request.POST['category_name']
        parent = request.POST['parent']

        category = Category(name=name, parent=parent)

        category.save()

        # message.success(request, 'Category added successfully')

        return redirect('/')

    else:
        # message.success(request, 'Operation Failed')
        return ;

