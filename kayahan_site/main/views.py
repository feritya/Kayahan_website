from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, KentselDonusumForm
from django.shortcuts import render
from .models import KentselDonusumBasvuru
from django.http import Http404


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()  # DB’ye kaydet

            # Mail gönder
            subject = f"Yeni İletişim Mesajı: {contact_message.subject}"
            message = f"""
            Gönderen: {contact_message.name}
            Email: {contact_message.email}

            Mesaj:
            {contact_message.message}
            """

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,   # Gönderen
                ["kamuranyasar13@gmail.com"],      # Hedef mail adresi
                fail_silently=False,
            )

            return render(request, "contact.html", {
                "form": ContactForm(), 
                "success": True
            })
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def kentsel_donusum_view(request):
    success = False

    if request.method == 'POST':
        form = KentselDonusumForm(request.POST, request.FILES)
        if form.is_valid():
            basvuru = form.save()

            send_mail(
                subject="Yeni Kentsel Dönüşüm Talebi",
                message=f"Yeni başvuru geldi: {basvuru.ad_soyad} - {basvuru.telefon}",
                from_email=None,
                recipient_list=['kamuranyasar13@gmail.com'],
            )

            return redirect('kentsel_donusum_success')
    else:
        form = KentselDonusumForm()

    return render(request, 'kentsel_donusum.html', {'form': form, 'success': success})

def kentsel_donusum_success(request):
    return render(request, 'kentsel_donusum_success.html')

# SEO uyumlu kentsel dönüşüm ilçeye göre
def kentsel_donusum_ilce(request, ilce):
    ilce = ilce.lower()

    izinli_ilceler = [
        "gungoren", "bagcilar", "bakirkoy", "bahcelievler", "esenler",
        "kucukcekmece", "basaksehir", "esenler", "zeytinburnu", "fatih",
        "eyupsultan", "bayrampasa", "kagithane", "sisli", "besiktas",
        "sariyer", "sultangazi", "avcilar", "silivri", "beylikduzu",
        "buyukcekmece", "sultangazi", "maltepe", "kartal", "pendik",
        "tuzla", "sancaktepe", "catalca", "arnavutkoy", "sile", "catalca"
    ]

    if ilce not in izinli_ilceler:
        raise Http404("Bu ilçe için içerik bulunamadı.")

    context = {
        "ilce": ilce.capitalize(),
    }

    return render(request, "kentsel_donusum_ilce.html", context)


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def projects(request):
    return render(request, "projects.html")


def custom_404_test(request):
    return render(request, "404.html", status=404)


# Hizmet Detayları
def service_kentsel(request):
    return render(request, "services/service-kentsel-donusum.html")

def service_konut(request):
    return render(request, "services/service-konut.html")

def service_magaza(request):
    return render(request, "services/service-magaza.html")

def service_interior(request):
    return render(request, "services/service-interior.html")

def service_mekanik(request):
    return render(request, "services/service-mekanik.html")

def service_site(request):
    return render(request, "services/service-site.html")

# Proje Detayları
def antalya_airport(request):
    return render(request, "projects/antalya-airport.html")
def arnavutkoy_bb(request):
    return render(request, "projects/arnavutkoy-bb.html")   
def koctas(request):
    return render(request, "projects/koctas.html")
def evidea(request):    
    return render(request, "projects/evidea.html")
def file(request):            
    return render(request, "projects/file.html")
def penti(request):               
    return render(request, "projects/penti.html")
def starbucks(request):               
    return render(request, "projects/starbucks.html")   
