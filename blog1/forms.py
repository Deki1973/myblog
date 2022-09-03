from django import forms
from .models import Postovi
# Day23
from django.contrib.auth.models import User
# day34 - kreiramo stranicu za unos i slanje komentara za post
from .models import Komentari


# Day 11
from .models import Kategorija
izbor=Kategorija.objects.all().values_list('naziv','naziv')
izbor_lista=[]
for i in izbor:
    izbor_lista.append(i)



class PostForm(forms.ModelForm):
    class Meta:
        model=Postovi
        fields=('naslov','naslov_tag','autor','kategorija','sadrzaj','snippet', 'header_slika')
        widgets = {
            'naslov': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Naslov posta'}),
            'naslov_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'test_elder', 'readonly': 'readonly'}),
            'kategorija':forms.Select(choices=izbor_lista, attrs={'class':'form-control'}),
            'sadrzaj': forms.Textarea(attrs={'class': 'form-control','placeholder':'Unestie sadrzaj ovde'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unestie sadrzaj ovde'}),
        }

class AzurirajPostForm(forms.ModelForm):
    class Meta:
        model=Postovi
        fields = ('naslov', 'naslov_tag', 'autor', 'sadrzaj','snippet',)
        widgets={
            'naslov': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Naslov posta'}),
            'naslov_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'test_elder_upd', 'readonly': 'readonly'}),
            'kategorija': forms.Select(attrs={'class': 'form-control'}),
            #'sadrzaj': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Unestie sadrzaj ovde'}),
            'snippet':forms.TextInput(attrs={'class':'form-control','placeholder':'Polje za isecak iz vaseg clanka'})

        }

class KomentarForm(forms.ModelForm):
    class Meta:
        model=Komentari
        fields=('sadrzaj',)
        # treba li datum dodavanja? - ne treba
        widgets={
            'post':forms.TextInput(attrs={'class':'form-control', 'placeholder':'post'}),
            'naslov':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Naslov posta'}),
            'sadrzaj':forms.Textarea(attrs={'class':'form-control','placeholder':'Unesite komentar ovde...'}),
        }