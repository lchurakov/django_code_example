from rest_framework import serializers

from .models import (
    Category,
    Courier,
    Favorite,
    Order,
    Product,
    Review,
    Shop,
    User,
    UserAddress
)


class UserAddressSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserAddress model.
    """

    class Meta:
        model = UserAddress
        fields = '__all__'


class UserAddressListSerializer(serializers.ListSerializer):
    """
    List serializer for UserAddress instances.
    """
    child = UserAddressSerializer()


class UserSerializer(serializers.ModelSerializer):
    """
       Serializer for the User model.
    """

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        """
        Validates the data before saving the User object.

        Additionally, checks that if the request method is PATCH and the 'user_name' field is passed,
        it should be in lowercase.

        Args:
            data (dict): Dictionary of data to validate.

        Returns:
            dict: Validated data.

        Raises:
            serializers.ValidationError: Validation error if conditions are not met.
        """
        user_name = data.get('user_name')

        if self.context['request'].method == 'PATCH' and user_name:
            if user_name.lower() != user_name:
                raise serializers.ValidationError("Поле 'user_name' должно быть в нижнем регистре.")

        return data


class UserListSerializer(serializers.ListSerializer):
    """
    List serializer for User instances.
    """
    child = UserSerializer()


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ListSerializer):
    """
    List serializer for Category instances.
    """
    child = CategorySerializer()


class ShopSerializer(serializers.ModelSerializer):
    """
    Serializer for the Shop model.
    """

    class Meta:
        model = Shop
        fields = '__all__'


class ShopListSerializer(serializers.ListSerializer):
    """
    List serializer for Shop instances.
    """
    child = ShopSerializer


class CourierSerializer(serializers.ModelSerializer):
    """
    Serializer for the Courier model.
    """

    class Meta:
        model = Courier
        fields = '__all__'


class CourierListSerializer(serializers.ListSerializer):
    """
    List serializer for Courier instances.
    """
    child = CourierSerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ListSerializer):
    """
    List serializer for Product instances.
    """
    child = ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    """

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ListSerializer):
    """
    List serializer for Order instances.
    """
    child = OrderSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favorite model.
    """

    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteListSerializer(serializers.ListSerializer):
    """
    List serializer for Favorite instances.
    """
    child = FavoriteSerializer


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    """

    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializer(serializers.ListSerializer):
    """
    List serializer for Review instances.
    """
    child = ReviewSerializer
