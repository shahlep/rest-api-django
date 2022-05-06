from django.http import JsonResponse
from .models import Library
from .serializers import LibrarySerializer

def book_list(request):
    #get all the books
    #serialize them
    #return json
