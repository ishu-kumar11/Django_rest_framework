from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Student
from .serializers import StudentSerializer


#Get request
class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	'''
	serializer_class = StudentSerializer means


		queryset = Student.objects.all()
		serializer = StudentSerializer(queryset, many=True)
		Response(serializer.data)

'''


#Post-> create student

class StudentCreate(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


#Retrive single object
#Ex: http://127.0.0.1:8000/students/5/

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#update
class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#delete
class StudentDestroyView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''

others generic views are:

ListCreateAPIView -> GET + POST
RetriveUpdateDestroyAPIView -> Get single object + PUT(update) + 															Delete

'''