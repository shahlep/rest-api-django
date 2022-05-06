from django.http import JsonResponse
from .models import Library
from .serializers import LibrarySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        # get all the books
        books = Library.objects.all()
        # serialize them
        serializer = LibrarySerializer(books, many=True)
        # return json
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
