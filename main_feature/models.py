from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100, unique=False)
    user_phone = models.CharField(max_length=10, unique=True)
    user_address = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'wupc_user'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'wupc_category'


class Part(models.Model):
    part_id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=100)
    part_description = models.CharField(max_length=200, null=True)
    part_price = models.IntegerField()
    part_image = models.ImageField(upload_to='images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.part_name

    class Meta:
        db_table = 'wupc_part'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_price = models.IntegerField()
    order_status = models.IntegerField()  # 0 = pending, 1 = paid, 2 = shipped, 3 = delivered, 4 = canceled
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user_name

    class Meta:
        db_table = 'wupc_order'


class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order_detail_quantity = models.IntegerField()
    order_detail_price = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_detail_id

    class Meta:
        db_table = 'wupc_order_detail'
