from django.contrib import admin

from .models import Rate


@admin.register(Rate)
class RefCodesAdmin(admin.ModelAdmin):
    pass
