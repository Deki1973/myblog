from django.shortcuts import render
# Day 9
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
#
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
# Day 20
from .forms import PrijavaForma
from django.http import HttpResponse
# Day 23
#prvi nacin
from django.contrib.auth.forms import UserChangeForm
from .forms import AzurirajProfilKorisnikaForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import AzurirajLozinkuForma2
# day 30
from django.views.generic import DetailView
from blog1.models import KorisnickiProfil
from django.shortcuts import get_object_or_404
# day 32
from django.views.generic import CreateView
from .forms import ProfilePageForm2

# day 32
class CreateProfilePageView(CreateView):
    model=KorisnickiProfil
    template_name = "clanovi/create_user_profle_page.html"
    #fields = '__all__' - stari nacin
    form_class = ProfilePageForm2
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)




# Create your views here.
class EditProfilePageView(generic.UpdateView):
    model = KorisnickiProfil
    template_name = 'clanovi/edit_profile_page.html'
    fields = ['bio','profil_slika', 'linkedin_url','fb_url','twitter_url']
    success_url = reverse_lazy('pocetna')



class PrikaziProfilnuStranicuView(DetailView):
    model=KorisnickiProfil
    template_name = 'clanovi/profil_korisnika.html'

    def get_context_data(self, *args, **kwargs):
        users=KorisnickiProfil.objects.all()
        context=super(PrikaziProfilnuStranicuView, self).get_context_data()
        #page_user=get_object_or_404(KorisnickiProfil, id=self.kwargs['pk'])
        page_user=get_object_or_404(KorisnickiProfil, id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context








class RegistracijaKorisnikaView(generic.CreateView):
    # form_class = UserCreationForm - stari nacin
    # Day 20
    form_class = PrijavaForma
    template_name = 'clanovi/registracija.html'
    success_url = reverse_lazy('pocetna')


def prijava_korisnika(request):
    print('prijava korisnika')
    if request.method == "POST":
        print("Metoda je POST")
        korisnicko_ime = request.POST['username']
        lozinka = request.POST['password']
        print(korisnicko_ime)
        print(lozinka)
        korisnik = authenticate(request, username=korisnicko_ime, password=lozinka)
        print('Autenifikacija')
        if korisnik is not None:
            print('Korisnik NIJE NONE')
            login(request, korisnik)
            # messages.success(request, (request,("DOBRODOSLI")))
            messages.success(request, "DOBRODOSLI. Uspesno ste se prijavili.")
            return redirect('pocetna')
        else:
            print('Korisnik je NONE')
            messages.success(request, ("Ooops! Pogresno korisnicko ime ili lozinka, ili nemate korisnicki nalog."))
            # return redirect('prijava')
            return render(request, 'clanovi/prijava.html', {})
    else:
        print("Metoda NIJE POST")
        return render(request, 'clanovi/prijava.html', {})


def odjava_korisnika(request):
    logout(request)
    messages.success(request, "Uspesna odjava.")
    print('Uspesna odjava')
    return redirect('pocetna')


def reg2(request):
    #return HttpResponse("REGISTRACIJA KORISNIKA")
    a='34343'
    return render(request,'clanovi/reg2.html',{'a':a,})


# Day 23
class AzurirajProfilView(generic.UpdateView):

    #form_class = UserChangeForm
    form_class = AzurirajProfilKorisnikaForm
    template_name = "clanovi/azuriraj_profil.html"
    success_url = reverse_lazy('pocetna')

    def get_object(self):
        return self.request.user




def uspesna_promena_lozinke(request):
    return render(request, 'clanovi/uspesna_promena_lozinke.html',{})

# Day 25 - Dodajemo funkcionalnost stranice za promenu lozinke
class PromenaLozinkeView(PasswordChangeView):
    #stari nacin: form_class = PasswordChangeForm
    form_class = AzurirajLozinkuForma2
    # kada je bolje razmislio, John je ipak odlucio da se vrati na stari nacin:
    #form_class = PasswordChangeForm
    template_name = 'clanovi/promeni_lozinku.html'
    success_url = reverse_lazy('uspesna-promena-lozinke')
