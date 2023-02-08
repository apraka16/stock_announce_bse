from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.stock_list_view),
    path('<int:scrip_id>', views.stock_announcement_list_view)
]
