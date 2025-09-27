from django.contrib import admin
from .models import BribeReport


@admin.register(BribeReport)
class BribeReportAdmin(admin.ModelAdmin):
    list_display = ('institution', 'reason', 'amount',
                    'reported_at', 'reporter_name', 'reporter_email')
    search_fields = ('institution', 'description')
    list_filter = ('reason', 'reported_at')
