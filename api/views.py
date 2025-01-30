from django.shortcuts import render
from .models import Note
from rest_framework import viewsets
from .serializer import NoteSerializer

# Create your views here.
def home(request):
  return render(request, 'base.html')

class NoteViewSet(viewsets.ModelViewSet):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer