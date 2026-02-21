from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', MenuListCreateView.as_view()),
    path('menu/<int:pk>/', MenuDetailView.as_view()),
    path('bookings/', BookingListCreateView.as_view()),
    path('bookings/<int:pk>/', BookingDetailView.as_view()),
]