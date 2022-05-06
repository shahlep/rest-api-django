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
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id):
    try:
        book = Library.objects.get(pk=id)
    except Library.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LibrarySerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LibrarySerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
