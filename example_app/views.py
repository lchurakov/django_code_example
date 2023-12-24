from rest_framework import viewsets
from django.utils import timezone

from .models import (
    UserAddress,
    User,
    Category,
    Shop,
    Courier,
    Product,
    Order,
    Favorite,
    Review
)

from .serializers import (
    UserAddressSerializer,
    UserSerializer,
    CategorySerializer,
    ShopSerializer,
    CourierSerializer,
    ProductSerializer,
    OrderSerializer,
    FavoriteSerializer,
    ReviewSerializer
)

from .signals import user_view_signal


class UserAddressViewSet(viewsets.ModelViewSet):
    """
        ViewSet for handling UserAddress objects.

        Provides CRUD operations for UserAddress model.

        Attributes:
            serializer_class (UserAddressSerializer): Serializer for UserAddress objects.

        Methods:
            get_queryset(): Retrieve the queryset for UserAddress objects.
        """
    serializer_class = UserAddressSerializer

    def get_queryset(self):
        return UserAddress.objects.all().select_related('user')


class UserViewSet(viewsets.ModelViewSet):
    """
        ViewSet for handling User objects.

        Provides CRUD operations for User model.

        Attributes:
            queryset (QuerySet): Queryset for User objects.
            serializer_class (UserSerializer): Serializer for User objects.

        Methods:
            get_queryset(): Retrieve the queryset for User objects.
            perform_create(serializer): Perform actions after creating a User.
            perform_update(serializer): Perform actions after updating a User.
            perform_destroy(instance): Perform actions before deleting a User.
        """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """Retrieve the queryset for User objects."""
        return User.objects.all()

    def perform_create(self, serializer):
        """Perform actions after creating a User."""
        serializer.save()
        user_view_signal.send(sender=self, user=serializer.instance)

    def perform_update(self, serializer):
        """Perform actions after updating a User."""
        serializer.instance.ts_spawn_changed = timezone.now()
        serializer.save()

    def perform_destroy(self, instance):
        """Perform actions before deleting a User."""
        instance.delete()


class CategoryViewSet(viewsets.ModelViewSet):
    """
     ViewSet for handling Category objects.

     Provides CRUD operations for Category model.

     Attributes:
         serializer_class (CategorySerializer): Serializer for Category objects.

     Methods:
         get_queryset(): Retrieve the queryset for Category objects.
     """
    serializer_class = CategorySerializer

    def get_queryset(self):
        """Retrieve the queryset for Category objects."""
        return Category.objects.all()


class ShopViewSet(viewsets.ModelViewSet):
    """
        ViewSet for handling Shop objects.

        Provides CRUD operations for Shop model.

        Attributes:
            serializer_class (ShopSerializer): Serializer for Shop objects.

        Methods:
            get_queryset(): Retrieve the queryset for Shop objects.
        """
    serializer_class = ShopSerializer

    def get_queryset(self):
        """Retrieve the queryset for Shop objects."""
        return Shop.objects.all().select_related('category')


class CourierViewSet(viewsets.ModelViewSet):
    """
        ViewSet for handling Courier objects.

        Provides CRUD operations for Courier model.

        Attributes:
            serializer_class (CourierSerializer): Serializer for Courier objects.

        Methods:
            get_queryset(): Retrieve the queryset for Courier objects.
        """
    serializer_class = CourierSerializer

    def get_queryset(self):
        """Retrieve the queryset for Courier objects."""
        return Courier.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """
        ViewSet for handling Product objects.

        Provides CRUD operations for Product model.

        Attributes:
            serializer_class (ProductSerializer): Serializer for Product objects.

        Methods:
            get_queryset(): Retrieve the queryset for Product objects.
        """
    serializer_class = ProductSerializer

    def get_queryset(self):
        """Retrieve the queryset for Product objects."""
        return Product.objects.all().select_related('shop')


class OrderViewSet(viewsets.ModelViewSet):
    """
       ViewSet for handling Order objects.

       Provides CRUD operations for Order model.

       Attributes:
           serializer_class (OrderSerializer): Serializer for Order objects.

       Methods:
           get_queryset(): Retrieve the queryset for Order objects.
       """
    serializer_class = OrderSerializer

    def get_queryset(self):
        """Retrieve the queryset for Order objects."""
        return Order.objects.all().select_related('user', 'product')


class FavoriteViewSet(viewsets.ModelViewSet):
    """
            ViewSet for handling Favorite objects.

            Provides CRUD operations for Favorite model.

            Attributes:
                serializer_class (FavoriteSerializer): Serializer for Favorite objects.

            Methods:
                get_queryset(): Retrieve the queryset for Favorite objects.
            """
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        """Retrieve the queryset for Favorite objects."""
        return Favorite.objects.all().select_related('user', 'product')


class ReviewViewSet(viewsets.ModelViewSet):
    """
       ViewSet for handling Review objects.

       Provides CRUD operations for Review model.

       Attributes:
           serializer_class (ReviewSerializer): Serializer for Review objects.

       Methods:
           get_queryset(): Retrieve the queryset for Review objects.
       """
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """Retrieve the queryset for Review objects."""
        return Review.objects.all().select_related('user', 'product')
