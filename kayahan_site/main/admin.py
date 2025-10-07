from django.contrib import admin
from .models import ContactMessage, KentselDonusumBasvuru
@admin.register(ContactMessage)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

@admin.register(KentselDonusumBasvuru)
class KentselDonusumFormAdmin(admin.ModelAdmin):
    list_display = ('ad_soyad', 'telefon', 'email', 'adres', 'tarih')
    search_fields = ('ad_soyad', 'telefon', 'email')
    list_filter = ('tarih',)
