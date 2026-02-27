from rest_framework.views import APIView #Class-based DRF View
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentList(APIView):

	def get(self, request):
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data) #converted JSON data

	def post(self, request):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)


#.data -> It gives you the final converted representation of the object.