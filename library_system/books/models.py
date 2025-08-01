from django.db import models


class Student(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=300)
    roll_no = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fname
    
class Book(models.Model):

    GENRE_CHOICES = [
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Science', 'Science'),
    ('Fantasy', 'Fantasy'),
    ('Biography', 'Biography'),
    ('Mystery', 'Mystery'),
    ('Other', 'Other'),
]
        
    book_id = models.IntegerField()
    title = models.CharField(max_length=230)
    is_avaliable = models.BooleanField(default=True)
    genre = models.CharField(choices=GENRE_CHOICES, default= 'Other')

    def __str__(self):
        return self.title


class Borrow_details(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned_date = models.DateField()
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return self.is_returned

# Create your models here.
