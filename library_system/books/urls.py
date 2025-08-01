from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, BookViewSet, BorrowDEtailsViewSet

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='students')
router.register(r'book', BookViewSet, basename='book')
router.register(r'borrow_details', BorrowDEtailsViewSet, basename='borrow_details')

urlpatterns = [
    path('', include(router.urls)),
]