from os import name
from django.urls import path

from .views import RealtorListView, RealtorDetailView, TopSellerView

app_name = 'realtors'

# Urlpatterns
urlpatterns = [
    path('topseller/', TopSellerView.as_view(), name='realtor_topseller'),
    path('<pk>/', RealtorDetailView.as_view(), name='realtor_detail'),
    path('', RealtorListView.as_view(), name='realtor_list'),
]