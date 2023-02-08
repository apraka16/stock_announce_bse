from django.urls import path, include

from stocks.views import StockViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stocks', StockViewSet)

urlpatterns = router.urls