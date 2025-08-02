from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, BookViewSet, BorrowDEtailsViewSet, get_book_list_for_particulat_student, student_borrow_limit,isbook_availiable

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='students')
router.register(r'book', BookViewSet, basename='book')
router.register(r'borrow_details', BorrowDEtailsViewSet, basename='borrow_details')

urlpatterns = [
    path('', include(router.urls)),
    path('borrowedbooks/<int:student_id>', get_book_list_for_particulat_student),
    path('student/<int:student_id>/borrow-limit/', student_borrow_limit),
    path('student/<int:book_id>/is_avail/', isbook_availiable),


]