from rest_framework import serializers
from .models import User, Product, Shipment, Order, ShipmentDetail, Admin, Address, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ShipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentDetail
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class BookSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'