from rest_framework.routers import DefaultRouter

from .views import (
    UserAddressViewSet,
    UserViewSet,
    CategoryViewSet,
    ShopViewSet,
    CourierViewSet,
    ProductViewSet,
    OrderViewSet,
    FavoriteViewSet,
    ReviewViewSet
)

router = DefaultRouter()
router.register(r'api/v1/user-addresses', UserAddressViewSet, basename='user-addresses')
router.register(r'api/v1/users', UserViewSet, basename='users')
router.register(r'api/v1/categories', CategoryViewSet, basename='categories')
router.register(r'api/v1/shops', ShopViewSet, basename='shops')
router.register(r'api/v1/couriers', CourierViewSet, basename='couriers')
router.register(r'api/v1/products', ProductViewSet, basename='products')
router.register(r'api/v1/orders', OrderViewSet, basename='orders')
router.register(r'api/v1/favorites', FavoriteViewSet, basename='favorites')
router.register(r'api/v1/reviews', ReviewViewSet, basename='reviews')
urlpatterns = router.urls
