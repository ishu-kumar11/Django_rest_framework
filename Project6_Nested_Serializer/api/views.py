from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookList(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)



'''
-output
[
    {
        "id": 1,
        "title": "Notes From Underground",
        "author": {
            "id": 1,
            "name": "Ishu"
        }
    },
    {
        "id": 2,
        "title": "Wild life",
        "author": {
            "id": 1,
            "name": "Ishu"
        }
    }
]
'''