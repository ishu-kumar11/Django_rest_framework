from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()              # Get queryset
    serializer = StudentSerializer(students, many=True)   # Create serializer
    return Response(serializer.data)              # Return JSON
