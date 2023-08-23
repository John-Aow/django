from django.shortcuts import render
from .serializers import UserSerializer, ProductSerializer, ShipmentSerializer, OrderSerializer, ShipmentDetailSerializer, AdminSerializer, AddressSerializer, BookSerailizer
from .models import User, Product, Shipment, Order,ShipmentDetail, Admin, Address, Book
from rest_framework import generics, viewsets, permissions, status
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response


# Create your views here.
class UserViews(viewsets.ViewSet):
    @staticmethod
    def list(request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serailizer = UserSerializer(user)
        return Response(serailizer.data)

    def update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = UserSerializer(user , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def partial_update(request, pk=None):
        pass

    def destroy(request, pk=None):
        pass
    