from django.urls import path
from .views import StudentList, StudentCreate, StudentRetrieve, StudentUpdateView, StudentDestroyView

urlpatterns = [
	path('students/', StudentList.as_view()),
	path('students/create/', StudentCreate.as_view()),
	path('students/<int:pk>/', StudentRetrieve.as_view()),
	path('students/<int:pk>/update/', StudentUpdateView.as_view()),
	path('students/<int:pk>/delete/', StudentDestroyView.as_view()),
]