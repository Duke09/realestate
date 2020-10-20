from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from .models import Realtor
from .serializers import RealtorSerailzer

# Create your views here.
class RealtorListView(ListAPIView):
    permissions_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerailzer
    pagination_class = None

class RealtorDetailView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerailzer

class TopSellerView(ListAPIView):
    permissions_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerailzer
    pagination_class = None