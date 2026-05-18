from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'appointment_date', 'appointment_time', 'whatsapp', 'created_at')
    list_filter = ('appointment_date', 'service', 'created_at')
    search_fields = ('name', 'whatsapp', 'service', 'comment')
    ordering = ('-appointment_date', '-appointment_time')
