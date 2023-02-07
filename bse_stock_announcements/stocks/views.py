from rest_framework import generics
from .models import Stock, Announcement
from .serializers import StockSerializer, AnnouncementSerializer


class StockListAPIView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

stock_list_view = StockListAPIView.as_view()

class StockAnnouncementListAPIView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    lookup_field = 'scrip.scrip_id'
    serializer_class = AnnouncementSerializer

stock_announcement_list_view = StockAnnouncementListAPIView.as_view()
