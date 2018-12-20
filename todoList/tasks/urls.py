from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoList.as_view(), name='todos'),
    path('todos/<int:pk>', views.TodoDetailsView.as_view(), name='todo'),
]
