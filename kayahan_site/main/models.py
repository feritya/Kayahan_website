from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class KentselDonusumBasvuru(models.Model):
    ad_soyad = models.CharField(max_length=150)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    adres = models.CharField(max_length=255)
    ada_no = models.CharField(max_length=50, blank=True, null=True)
    parsel_no = models.CharField(max_length=50, blank=True, null=True)
    bina_yasi = models.PositiveIntegerField()
    daire_sayisi = models.PositiveIntegerField()
    aciklama = models.TextField(blank=True, null=True)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad_soyad} - {self.adres}"

