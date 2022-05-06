from django.http import JsonResponse
from .models import Library
from .serializers import LibrarySerializer
from rest_framework.decorators import api_view


@api_view('GET', 'POST')
def book_list(request):
    # get all the books
    books = Library.objects.all()
    # serialize them
    serializer = LibrarySerializer(books, many=True)
    # return json
    return JsonResponse(serializer.data, safe=False)
