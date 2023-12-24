# Generated by Django 5.0 on 2023-12-24 13:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30)),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('courier_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('user_first_name', models.CharField(max_length=30)),
                ('user_last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[(1, 'Покупатель'), (2, 'Администратор магазина'), (3, 'Администратор маркетплейса')], default=1, max_length=1)),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.category')),
                ('shops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=500)),
                ('rating', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, max_length=1)),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.product')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('couriers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='example_app.courier')),
                ('products', models.ManyToManyField(to='example_app.product')),
                ('shops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.shop')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('favorite_id', models.AutoField(primary_key=True, serialize=False)),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('building', models.CharField(max_length=255)),
                ('apartment', models.CharField(max_length=255)),
                ('ts_spawn', models.DateTimeField(default=django.utils.timezone.now)),
                ('ts_spawn_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('users', models.ManyToManyField(to='example_app.user')),
            ],
        ),
    ]