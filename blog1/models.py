import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



class Kategorija(models.Model):
    naziv=models.CharField(max_length=255)

    def __str__(self):
        return self.naziv

    def get_absolute_url(self):
        return reverse('pocetna')

# Create your models here.

class Postovi(models.Model):
    class Meta:
        verbose_name_plural = 'Postovi'

    naslov=models.CharField(max_length=255)
    header_slika=models.ImageField(null=True, blank=True, upload_to="images/")
    naslov_tag=models.CharField(max_length=255, null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #sadrzaj=models.TextField(null=True, blank=True)
    sadrzaj=RichTextField(blank=True, null=True)
    datum=models.DateTimeField(auto_now_add=datetime.datetime.now())
    # Day 12 - dodajemo kategoriju bloga
    kategorija=models.CharField(max_length=255, default='Ostalo')
    # Day 18
    lajkovi=models.ManyToManyField(User, related_name='blogposts')
    # Day 22
    snippet=models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.naslov + ' | '+str(self.autor)

    def get_absolute_url(self):
        return reverse('detaljna', args=(str(self.id)))

    def ukupno_lajkova(self):
        return self.lajkovi.count()


class Komentari(models.Model):
    post=models.ForeignKey(Postovi, on_delete=models.CASCADE, related_name="komentari")
    ime_komentatora=models.CharField(max_length=255)
    sadrzaj=models.TextField()
    datum_komentara=models.DateTimeField(auto_now_add=True)
    # da probam da dodam lajkove za komentar
    lajkovi_za_koment=models.ManyToManyField(User, related_name="blogcomments")


    def __str__(self):
        return '%s - %s - %s - %s' % (self.post.naslov, self.ime_komentatora,self.sadrzaj, self.datum_komentara)

    def ukupno_lajkova_za_komentar(self):
        return self.lajkovi_za_koment.count()

# da probam da dodam lajkove na komentare




class KorisnickiProfil(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profil_slika = models.ImageField(null=True, blank=True, upload_to="images/profilke/")
    linkedin_url=models.CharField(max_length=255, null=True, blank=True)
    fb_url= models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)+' | '+str(self.bio)   #mora kasovanje jer je polje upotrebljeno kako kljuc

    def get_absolute_url(self):
        return reverse('pocetna')

