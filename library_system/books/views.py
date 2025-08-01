from django.shortcuts import render
from rest_framework import viewsets
from .serilizers import Studentserializer, Bookserializers, BorrowdetailsSerializers
from .models import Student, Book, Borrow_details

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializers

class BorrowDEtailsViewSet(viewsets.ModelViewSet):
    queryset = Borrow_details.objects.all()
    serializer_class = BorrowdetailsSerializers