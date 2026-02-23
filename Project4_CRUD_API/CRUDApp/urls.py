from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_students),
    path('students/<int:pk>/', views.get_student),
    path('students/create/', views.create_student),
    path('students/update/<int:pk>/', views.update_student),
    path('students/delete/<int:pk>/', views.delete_student),
]