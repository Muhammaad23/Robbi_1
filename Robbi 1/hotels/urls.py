from django.urls import path
from .views import HotelsView, HotelsDetailView

urlpatterns = [
    path('hotels/', HotelsView.as_view(), name='hotels-list'),  # List and create hotels
    path('hotels/<int:pk>/', HotelsDetailView.as_view(), name='hotels-detail'),

]
