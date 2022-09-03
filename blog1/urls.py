from django.urls import path
from . import views
from . views import PocetniView
from .views import ArticleDetailView
from .views import NoviPostView
from .views import AzurirajPostView
from .views import ObrisiPostView
from .views import NovaKategorija
from .views import Kategorija
from .views import NoviKomentarView


urlpatterns=[
    #path('pocetna/', views.pocetna, name="pocetna"),
    path('pocetna/', PocetniView.as_view(), name="pocetna"),
    path('detaljna/<int:pk>', ArticleDetailView.as_view(), name="detaljna"),
    path('novi_post', NoviPostView.as_view(), name="novi-post"),
    path('detaljna/edit/<int:pk>', AzurirajPostView.as_view(), name="azuriraj-post"),
    path('obrisi_post/<int:pk>', ObrisiPostView.as_view(), name="obrisi-post"),
    path('nova_kategorija/', NovaKategorija.as_view(), name="nova-kategorija"),
    path('kategorija/<str:kateg>/', views.KategorijaView, name="kategorija"),
    path('kategorije_spisak', views.prikazi_spisak_kategorija, name="kategorije-spisak"),
    path('lajkuj_post/<int:pk>', views.lajkuj, name="lajkuj-post"),
    #path('detaljna/<int:pk>/komentar/', NoviKomentarView.as_view(), name="novi-komentar"),
    path('detaljna/<int:pk><str:user>/komentar/', views.dodaj_komentar_view_2, name="novi-komentar"),
    path('pretraga_postova', views.pretraga_postova, name="pretraga-postova"),
    path('lajkuj_komentar/<int:komentpk> <int:objectpk>', views.lajkuj_komentar, name="lajkuj-komentar"),
    #path('detaljna/<int:pk> <str:ukupno_lajkova>', ArticleDetailView.as_view(), name="detaljna"),
    ]