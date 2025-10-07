from django import forms
from .models import ContactMessage, KentselDonusumBasvuru

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Adınız"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Konu"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Mesajınız", "rows": 5}),
        }


class KentselDonusumForm(forms.ModelForm):


    class Meta:
        model = KentselDonusumBasvuru
        fields = ['ad_soyad', 'telefon', 'email', 'adres', 'ada_no', 'parsel_no', 'bina_yasi', 'daire_sayisi', 'aciklama']
        widgets = {
            'ad_soyad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad Soyad'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta'}),
            'adres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adres'}),
            'ada_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ada No (Varsa)'}),
            'parsel_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Parsel No (Varsa)'}),
            'bina_yasi': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bina Yaşı'}),
            'daire_sayisi': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Daire Sayısı'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ek Bilgi (İsteğe Bağlı)', 'rows': 4}),
        }
