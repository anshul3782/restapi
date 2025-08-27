from django.contrib import admin
from .models import CheckinData

@admin.register(CheckinData)
class CheckinDataAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'steps', 'heart_rate', 'mood', 'created_at')
    list_filter = ('created_at', 'mood')
    search_fields = ('phone_number',)
