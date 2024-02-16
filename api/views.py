# api\views.py
from django.shortcuts import render
from rest_framework import viewsets

from .models import User, Order
from .serializers import UserSerializer, OrderSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


############### viewSet for Order ############
class OrderViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # filter, urls e api/orders/1  : ehane "1" id, ei id hishebe filter
    def get_queryset(self):
        queryset = Order.objects.all()
        id=self.request.query_params.get("id",None)

        if id is not None:
            queryset = queryset.filter(user__id=id)

        return queryset
