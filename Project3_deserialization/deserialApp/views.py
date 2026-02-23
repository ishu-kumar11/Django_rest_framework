from django.http import HttpResponse
from django.core import serializers
from .models import Student
import json

def deserialize_demo(request):

    json_data = '''
    [
      {
        "model": "deserialApp.student",
        "pk": 1,
        "fields": {
          "name": "Ishu",
          "age": 19
        }
      },
      {
        "model": "deserialApp.student",
        "pk": 2,
        "fields": {
          "name": "Rahul",
          "age": 21
        }
      }
    ]
    '''

    # JSON → Django objects
    stream = json.loads(json_data)
    for obj in serializers.deserialize("json", json.dumps(stream)):
        obj.save()

    students = Student.objects.all()

    output = ""
    for s in students:
        output += f"Name: {s.name}, Age: {s.age} <br>"

    return HttpResponse(output)