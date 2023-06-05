# Generated by Django 4.2 on 2023-05-12 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("category_id", models.AutoField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=100)),
                ("category_description", models.CharField(max_length=200, null=True)),
            ],
            options={
                "db_table": "wupc_category",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                ("order_price", models.IntegerField()),
                ("order_status", models.IntegerField()),
            ],
            options={
                "db_table": "wupc_order",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("user_name", models.CharField(max_length=100)),
                ("user_email", models.CharField(max_length=100)),
                ("user_phone", models.CharField(max_length=10, unique=True)),
                ("user_address", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "wupc_user",
            },
        ),
        migrations.CreateModel(
            name="Part",
            fields=[
                ("part_id", models.AutoField(primary_key=True, serialize=False)),
                ("part_name", models.CharField(max_length=100)),
                ("part_description", models.CharField(max_length=200, null=True)),
                ("part_price", models.IntegerField()),
                ("part_image", models.ImageField(null=True, upload_to="images/")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_feature.category",
                    ),
                ),
            ],
            options={
                "db_table": "wupc_part",
            },
        ),
        migrations.CreateModel(
            name="OrderDetail",
            fields=[
                (
                    "order_detail_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("order_detail_quantity", models.IntegerField()),
                ("order_detail_price", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_feature.order",
                    ),
                ),
                (
                    "part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_feature.part",
                    ),
                ),
            ],
            options={
                "db_table": "wupc_order_detail",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main_feature.user"
            ),
        ),
    ]
