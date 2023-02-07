from django.urls import path, include
from . import views
from user import views as user_views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("products", views.ProductsViewSet)
router.register("categories", views.CategoryViewSet)
router.register('user', user_views.UserViewSet)


urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls))
]