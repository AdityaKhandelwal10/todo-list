
# from django.shortcuts import render
from winreg import CreateKeyEx
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import  LoginRequiredMixin

from .models import Task

#login view 
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


# We will be creating class based view TaskList here which will extend the List View
# We dont have to specify a view as well, it automatically looks for it

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

#The detailview class will provide detailed view
# looks for <model>_detail.html 
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'


#We create items here with this class by extending the CreateView class
# We will be using model forms here and specify the fields that we want
# We want to redirect the user after it has successfully submitted a form, we will use reverse lazy for that

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

#Update view -> Uses a prefilled form which we will update
#Looks for the same template as create view, but here it provides a prepopulated form
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

