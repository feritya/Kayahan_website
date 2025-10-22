"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    # Admin Panel
    path('admin-panel/', admin.site.urls),

        # Ana Sayfa ve Diğer Sayfalar
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('projects/', views.projects, name="projects"),
    path("test-404/", views.custom_404_test, name="test-404"),

    # Kentsel Dönüşüm Başvuru Sayfası
    path('kentsel-donusum/',views.kentsel_donusum_view, name='kentsel_donusum'),
    path('kentsel-donusum/success/', views.kentsel_donusum_success, name='kentsel_donusum_success'),



    #hizmet detay sayfaları :
    path("services/kentsel-donusum/", views.service_kentsel, name="service_kentsel"),
    path("services/konut-projeleri/", views.service_konut, name="service_konut"),
    path("services/magaza-ofis/", views.service_magaza, name="service_magaza"),
    path("services/ic-mimarlik/", views.service_interior, name="service_interior"),
    path("services/mekanik/", views.service_mekanik, name="service_mekanik"),
    path("services/santiye-yonetimi/", views.service_site, name="service_site"),

    #proje detay sayfaları :
    path("projects/antalya-airport/", views.antalya_airport, name="antalya_airport"),
    path("projects/arnavutkoy-bb/", views.arnavutkoy_bb, name="arnavutkoy_bb"),
    path("projects/koctas/", views.koctas, name="koctas"),
    path("projects/eidea/", views.evidea, name="evidea"),
    path("projects/file/", views.file, name="file"),
    path("projects/penti/", views.penti, name="penti"),
    path("projects/starbucks/", views.starbucks, name="starbucks"),

    # seo uyumlu url'ler
    path('kentsel-donusum/<str:ilce>/', views.kentsel_donusum_ilce, name='kentsel_donusum_ilce'),


    

]
