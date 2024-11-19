from django.urls import path
from .views import HotelView, HotelDetailView

urlpatterns = [
    path('hotel/', HotelView.as_view(), name='hotel-list'),  # List and create hotel
    path('hotel/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),

]
