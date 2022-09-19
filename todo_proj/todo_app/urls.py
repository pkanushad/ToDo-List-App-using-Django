from django.contrib import admin
from django.urls import path,include
from todo_app import views
from .views import TaskList
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.CustomLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('register/',views.RegisterPage.as_view(),name="register"),

    path('',views.TaskList.as_view(),name="tasks" ),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name="task"),
    path('create-task/',views.TaskCreate.as_view(),name="task-create" ),
    path('create-update/<int:pk>/',views.TaskUpdate.as_view(),name="task-update" ),
    path('create-delete/<int:pk>/',views.DeleteView.as_view(),name="task-delete" ),


]
