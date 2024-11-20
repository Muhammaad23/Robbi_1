from django.urls import path, include
from .views import HotelView, HotelDetailView
from rest_framework.routers import DefaultRouter
from hotels.views import MehmonxonaViewSet


router = DefaultRouter()
router.register(r'mehmonxona', MehmonxonaViewSet)

urlpatterns = [
    path('hotels/', include(router.urls)),
    path('hotel/', HotelView.as_view(), name='hotel-list'),  # List and create hotel
    path('hotel/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),

]
