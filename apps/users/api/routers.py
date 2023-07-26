from rest_framework.routers import DefaultRouter
from apps.users.api.views import HouseViewSet, UserViewSet

router = DefaultRouter()

router.register(r'houses',HouseViewSet, basename='houses')
router.register(r'users',UserViewSet, basename='users')

urlpatterns = router.urls