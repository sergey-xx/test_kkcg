from django.contrib import admin

from .models import Rate


@admin.register(Rate)
class RefCodesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'charcode', 'rate', 'date')
    list_filter = ('charcode', 'date')
