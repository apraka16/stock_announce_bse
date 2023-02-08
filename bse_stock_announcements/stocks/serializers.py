from rest_framework import serializers
from .models import Stock, Announcement

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'pk',
            'scrip_id',
            'scrip_long_name',
        ]

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            'scrip_id',
            'timestamp',
            'news_stub',
            'news_headline',
        ]