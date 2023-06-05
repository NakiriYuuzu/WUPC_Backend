from rest_framework import serializers

from main_feature.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'category_description']


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['part_id', 'part_name', 'part_description', 'part_price', 'part_image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'user_phone', 'user_address']


class OrderDetailSerializer(serializers.ModelSerializer):
    part = PartSerializer()

    class Meta:
        model = OrderDetail
        fields = ['order_detail_quantity', 'order_detail_price', 'part']


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    order_details = OrderDetailSerializer(source='orderdetail_set', many=True)
    order_status_display = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['order_id', 'order_date', 'order_price', 'order_status_display', 'user', 'order_details']

    @staticmethod
    def get_order_status_display(obj):
        status_dict = {
            0: '未付款',
            1: '已付款',
            2: '出貨中',
            3: '已送達',
            99: '棄單',
        }
        return status_dict.get(obj.order_status, '未知狀態')


class CartItemSerializer(serializers.Serializer):
    part_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CheckoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=200)
    carts = CartItemSerializer(many=True)
