from django.urls import path
from .views import RegistracijaKorisnikaView
from .views import AzurirajProfilView
from . import views
from .views import PromenaLozinkeView
# day 30
from .views import PrikaziProfilnuStranicuView
from .views import EditProfilePageView
from .views import CreateProfilePageView


urlpatterns=[
    #path('registracija', RegistracijaKorisnikaView.as_view(), name="registracija"),
    path('prijava', views.prijava_korisnika, name="prijava"),
    path('odjava', views.odjava_korisnika, name="odjava"),
    path('registracija',RegistracijaKorisnikaView.as_view(),name="registracija"),#nije moglo da radi, verovatno jer je r'"regissracija" vec bilo upotrebljeno negde kao kljucna rec
    #path('reg2', views.reg2, name="reg2"),
    path('reg2',RegistracijaKorisnikaView.as_view(),name="reg2"),
    path('azuriranje_profila', AzurirajProfilView.as_view(), name="azuriranje-profila"),
    path('promena_lozinke',PromenaLozinkeView.as_view(),name="promena-lozinke"),
    path('uspesna_promena_lozinke', views.uspesna_promena_lozinke, name="uspesna-promena-lozinke"),
    path('<int:pk>/profile/', PrikaziProfilnuStranicuView.as_view(), name="prikazi-profilnu-stranicu"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit-profile-page"),
    #path('create_profile_page/', CreateProfilePageView.as_view(), name="create-profile-page"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name="create-profile-page"),
]