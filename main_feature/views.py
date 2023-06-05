from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *


class CategoryView(APIView):
    @staticmethod
    def get(request):
        mode = request.query_params.get('mode', None)
        if mode:
            categories = Category.objects.filter(category_description__isnull=True)
        else:
            categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PartView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        category = request.query_params.get('category', None)

        if category:
            parts = Part.objects.filter(category_id=category)
        else:
            parts = Part.objects.all()

        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderView(APIView):
    @staticmethod
    def get(request):
        phone = request.GET.get('phone', None)

        if phone is None:
            return Response({"message": "Phone Number('phone') is required"}, status=status.HTTP_400_BAD_REQUEST)

        orders = Order.objects.filter(user__user_phone=phone)

        if not orders.exists():
            return Response({"message": "No order found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            phone = serializer.validated_data.get('phone')
            address = serializer.validated_data.get('address')
            carts = serializer.validated_data.get('carts')

            user, created = User.objects.update_or_create(
                user_phone=phone,
                defaults={'user_name': name, 'user_email': email, 'user_address': address}
            )

            orders = Order.objects.create(user=user, order_price=0, order_status=0)

            total_price = 0

            for cart in carts:
                part = Part.objects.get(part_id=cart['part_id'])
                OrderDetail.objects.create(
                    order_id=orders.order_id,
                    part_id=part.part_id,
                    order_detail_price=part.part_price,
                    order_detail_quantity=cart['quantity']
                )

                total_price += part.part_price * cart['quantity']

            orders.order_price = total_price
            orders.save()

            return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
