from django.contrib import admin
from .models import Postovi
from .models import Kategorija
from .models import KorisnickiProfil
from .models import Komentari

# Register your models here.
admin.site.register(Postovi)
admin.site.register(Kategorija)
admin.site.register(KorisnickiProfil)
admin.site.register(Komentari)