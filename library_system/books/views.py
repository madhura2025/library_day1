from django.shortcuts import render
from rest_framework import viewsets
from .serilizers import Studentserializer, Bookserializers, BorrowdetailsSerializers
from .models import Student, Book, Borrow_details
from rest_framework.decorators import api_view
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializers

class BorrowDEtailsViewSet(viewsets.ModelViewSet):
    queryset = Borrow_details.objects.all()
    serializer_class = BorrowdetailsSerializers

@api_view(['GET'])
def get_book_list_for_particulat_student(request, student_id):
    student = Student.objects.get(id=student_id)
    borrowed_book = Borrow_details.objects.filter(student_id=student, returned_date__isnull=True)
    serializer = BorrowdetailsSerializers(borrowed_book, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def student_borrow_limit(request, student_id):
    student = Student.objects.get(id=student_id)
    borrowed_count = Borrow_details.objects.filter(student_id=student, returned_date__isnull=True).count()
    return Response({"borrow_limit": borrowed_count})

@api_view(['GET'])
def isbook_availiable(request, book_id):
    book = Book.objects.get(id=book_id)
    isavaliable = Borrow_details.objects.filter(is_returned=True)
    # serializer = BorrowdetailsSerializers(isavaliable)
    return Response(isavaliable)
