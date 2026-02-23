from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student


#GET ALL STUDENTS
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    data = []

    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "age": s.age,
            "course": s.course
        })

    return Response(data)


#GET SINGLE STUDENT
@api_view(['GET'])
def get_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"})

    data = {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    return Response(data)


#CREATE STUDENT (POST)
@api_view(['POST'])
def create_student(request):
    name = request.data.get('name')
    age = request.data.get('age')
    course = request.data.get('course')

    student = Student.objects.create(
        name=name,
        age=age,
        course=course
    )

    return Response({
        "message": "Student created",
        "id": student.id
    })


# UPDATE STUDENT (PUT & PATCH)
@api_view(['PUT', 'PATCH'])
def update_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"})

    name = request.data.get('name')
    age = request.data.get('age')
    course = request.data.get('course')

    if name is not None:
        student.name = name
    if age is not None:
        student.age = age
    if course is not None:
        student.course = course

    student.save()

    return Response({"message": "Student updated"})


# DELETE STUDENT
@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"})

    student.delete()

    return Response({"message": "Student deleted successfully"})