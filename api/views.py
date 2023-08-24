from django.shortcuts import render
from .serializers import UserSerializer, ProductSerializer, ShipmentSerializer, OrderSerializer, ShipmentDetailSerializer, AdminSerializer, AddressSerializer, BookSerailizer, CreateOrderSerializer
from .models import User, Product, Shipment, Order,ShipmentDetail, Admin, Address, Book
from rest_framework import generics, viewsets, permissions, status
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import datetime


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
        pass

    def partial_update(request, pk=None):
        pass

    def destroy(request, pk=None):
        pass
    
class ProductViews(viewsets.ViewSet):
    @staticmethod
    def list(request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serailizer = ProductSerializer(product)
        return Response(serailizer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(request, pk=None):
        pass

    def destroy(request, pk=None):
        pass

class OrderViews(viewsets.ViewSet):
    @staticmethod
    def list(request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            user = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serailizer = OrderSerializer(user)
        return Response(serailizer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(request, pk=None):
        pass

    def destroy(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CheckoutViews(viewsets.ViewSet):
    @staticmethod
    def list(request):
        pass

    def create(self, request):
        now = datetime.datetime.now()
        temp = {
            
        }
        shipment = OrderSerializer(
            data=temp
        )
        if shipment.is_valid():
            shipment.save()
            return Response(shipment.data)
        return Response(shipment.errors)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(request, pk=None):
        pass

    def destroy(request, pk=None):
        pass