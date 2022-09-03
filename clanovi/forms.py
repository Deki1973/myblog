from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# Day 23
from django.contrib.auth.forms import UserChangeForm
#Day 25
from blog1.models import KorisnickiProfil
from django.contrib.auth.forms import PasswordChangeForm
# day 32
from django.db import models


class ProfilePageForm2(forms.ModelForm):
    class Meta:
        model=KorisnickiProfil
        #necemo user-a, vec da ta vrednost bude automatska
        fields=('bio','profil_slika','linkedin_url','fb_url','twitter_url',)



        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            #'profil_slika':forms.ImageField(attrs={'class':'form-control'}),
            'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
            'fb_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
        }


#hocemo da izbacimo polje autor da se automatski
class ProfilePageForm1(forms.ModelForm):
    model=KorisnickiProfil
    fields=('bio','profil_slika','linkedin_url','fb_url','twitter_url')
    bio=models.TextField(null=True,blank=True)
    profil_slika=models.ImageField(null=True, blank=True, upload_to='images/profilke/')
    linkedin_url=models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    widgets={
        'bio':forms.Textarea(attrs={'class':'form-control'}),
        #'profil_slika':forms.TextInput()
        'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
        'fb_url':forms.TextInput(attrs={'class':'form-control'}),
        'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
    }


class PrijavaForma(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(PrijavaForma, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




class AzurirajProfilKorisnikaFormORIGINAL(UserChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check','null':'True'}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check', 'null':'True'}))
    is_active=forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check', 'null':'True'}))
    date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))



    #password = None
    class Meta:
        model = User
        fields=('username','first_name','last_name','password','last_login','is_superuser','is_staff','is_active','date_joined')

        #fields = ["username", "email", "first_name", "last_name"]
        # fields = ["username", "email", "first_name", "last_name", "profile_pic"]

class AzurirajProfilKorisnikaForm(UserChangeForm):
    # password = None
    class Meta:
        model = KorisnickiProfil
        fields = (
        'username', 'email', 'first_name', 'last_name', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active',
        'date_joined', 'bio')

    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check','blank':'True'}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check', 'blank':'True'}))
    is_active=forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check', 'blank':'True'}))
    date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #bio=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    bio =forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))




        #fields = ["username", "email", "first_name", "last_name"]
        # fields = ["username", "email", "first_name", "last_name", "profile_pic"]





class AzurirajLozinkuForma2(PasswordChangeForm):
    #stara_lozinka=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    #nova_lozinka_1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    #nova_lozinka_2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    #nova_lozinka_1 = forms.CharField()
    #nova_lozinka_2 = forms.CharField()
    #
    # MORA ENGLESKI !!!
    #
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Stara lozinka','label':''}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Stara lozinka','label':''}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Stara lozinka','label':''}))
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')
        #Ovo ispod nije htelo da radi iz za sada nepoznatih razloga:
        #labels = {
        #    'old_password': 'Unesite staru lozinku',
        #    'new_password1': 'Unesite novu lozinku',
        #    'new_password2': 'Potvrdite novu lozinku',
        #}
        # Ovo ispod nije htelo da radi iz za sada nepoznatih razloga
        #widgets={
        #    'old_password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Stara lozinka'}),
        #    'new_password1': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Nova lozinka'}),
        #    'new_password2': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Potvrda Nova lozinka'}),
        #}





