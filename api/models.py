import uuid
from django.db import models

# Create your models here.
class Note(models.Model): 
    id = models.UUIDField(max_length=30, primary_key=True, default=uuid.uuid4, editable=False) # o id é gerado automaticamete pelo UUID
    note = models.TextField()
    date = models.DateField(auto_now_add=True)

