from django.contrib import admin
from .models import Stock, Announcement

# Register your models here.
admin.site.register(Stock)
admin.site.register(Announcement)
