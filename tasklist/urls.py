from django.urls import path
from . import views

urlpatterns = [
	# path('', views.index, name='index'),
    path('login/', views.signup, name='login'),
    path('u/<str:username>', views.index, name='user_page'),
    path('u/<str:username>/completed', views.completedPage, name='completed_page'),
    path('mytask/create', views.createTask, name='create_task'),
    path('mytask/delete', views.deleteTask, name='delete_task'),
    path('mytask/update', views.updateTask, name='update_task'),
    path('mytask/complete', views.completeTask, name='complete_task'),
]