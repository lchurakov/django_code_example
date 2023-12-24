from django.db import models
from django.utils import timezone


class TimestampMixin(models.Model):
    """Mixin with timestamp fields."""
    ts_spawn = models.DateTimeField(default=timezone.now)
    ts_spawn_changed = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class UserAddress(TimestampMixin, models.Model):
    """Model for user addresses."""
    address_id = models.AutoField(primary_key=True)
    apartment = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    users = models.ManyToManyField('User')


class User(TimestampMixin, models.Model):
    """Model for user information."""
    ACCESS_CHOICES = (
        (1, 'Покупатель'),
        (2, 'Администратор магазина'),
        (3, 'Администратор маркетплейса'),
    )

    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    registration_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=1, choices=ACCESS_CHOICES, default=1, null=False)
    user_first_name = models.CharField(max_length=30)
    user_id = models.AutoField(primary_key=True)
    user_last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.user_last_name} {self.user_first_name}'


class Category(TimestampMixin, models.Model):
    """Model for product categories."""
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Shop(TimestampMixin, models.Model):
    """Model for shops."""
    location = models.CharField(max_length=255)
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=255)

    def __str__(self):
        return self.shop_name


class Courier(TimestampMixin, models.Model):
    """Model for couriers."""
    courier_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(TimestampMixin, models.Model):
    """Model for products."""
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.CharField(max_length=500)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    shops = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Order(TimestampMixin, models.Model):
    """Model for orders."""
    comment = models.CharField(max_length=255)
    couriers = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(default=timezone.now)
    order_id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField()
    shops = models.ForeignKey(Shop, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order # {self.order_id} from {self.order_date}'


class Favorite(TimestampMixin, models.Model):
    """Model for user favorites."""
    favorite_id = models.AutoField(primary_key=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(TimestampMixin, models.Model):
    """Model for product reviews."""
    ACCESS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    comment = models.CharField(max_length=500)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=ACCESS_CHOICES, default=1, null=False)
    review_id = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
