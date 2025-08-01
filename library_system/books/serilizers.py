from rest_framework import serializers
from .models import Student, Book, Borrow_details

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowdetailsSerializers(serializers.ModelSerializer):
    student = Studentserializer(read_only = True)
    book = Bookserializers(read_only = True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student'
    )
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book'
    )

    class Meta:
        model = Borrow_details
        fields = ['id', 'student', 'book', 'student_id', 'book_id', 'borrow_date', 'due_date', 'returned_date', 'is_returned']