
# from django.shortcuts import render
from winreg import CreateKeyEx
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

    #For user specific data, we get the context pbject and filter it
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user= self.request.user)
        # context['count'] = context['task'].filter(complete = False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains = search_input)

        context['search_input'] =search_input
        return context

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
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

#Update view -> Uses a prefilled form which we will update
#Looks for the same template as create view, but here it provides a prepopulated form
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class RegisterUserView(FormView):
    template_name = 'base/register.html' 
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(RegisterUserView, self).form_valid(form)

    #Overriding, if we are already logged in we do not wanna see this register page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterUserView, self).get() #do as it was supposed to 