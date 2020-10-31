from django.urls import path, include
from rest_framework import routers
from .views import ProductView

router = routers.DefaultRouter()
router.register('', ProductView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
