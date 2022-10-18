from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name = 'tasks'),
    path('login/', views.CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('register/', views.RegisterUserView.as_view(), name = 'register'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name = 'task-detail'), #It looks for <int:pk> as default
    path('task-create/', views.TaskCreateView.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', views.TaskDeleteView.as_view(), name = 'task-delete'),
    
    
]
