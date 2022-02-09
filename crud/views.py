from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from crud import models
from django.urls import reverse_lazy

# Create your views here.

class Index(ListView):
    context_object_name='employess'
    model=models.Employee_List_Database
    template_name='index.html'

class Add_employee(CreateView):
    model=models.Employee_List_Database
    fields=('__all__')
    template_name='insert.html'

class Update_employee(UpdateView):
    context_object_name='employess'
    model=models.Employee_List_Database
    fields=('__all__')
    template_name='update.html'

class Delete(DeleteView):
    context_object_name='employess'
    model=models.Employee_List_Database
    success_url=reverse_lazy('crud:index')
    template_name='delete.html'
