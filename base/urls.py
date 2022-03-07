import imp
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView, TaskDelete, TaskDetail, TaskList, TaskCreate, TaskUpdate, apiList

urlpatterns = [
    #  This is for react part
    path('api/', apiList, name='api-overview'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    # In django, pk is the primary key attribute in the table
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    # the name attribute is an statement so that the html part can call the name for jump to this page
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('task_update/<int:pk>', TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>', TaskDelete.as_view(), name='task_delete'),
]