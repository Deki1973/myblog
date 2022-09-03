from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Postovi
from .forms import PostForm
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy, reverse
from .forms import AzurirajPostForm
# day 33
from .models import Komentari
from .forms import KomentarForm
from django.contrib import messages
from django.shortcuts import redirect

# experiment
from django.contrib.auth.models import User

# Create your views here.


# Day 12
from .models import Kategorija
# Day 18
# Day 20
# Day 23
from django.views.generic import UpdateView
#
from django.core.paginator import Paginator



#def pocetna(request):
#    return render(request,'blog1/pocetna.html',{})
# Day x1
from django.db import connection

# Day 18

def lajkuj(request, pk):
    p=get_object_or_404(Postovi, id=request.POST.get('post_id'))
    lajkovano=False
    if p.lajkovi.filter(id=request.user.id).exists():
        p.lajkovi.remove(request.user)
        lajkovano=False
    else:
        p.lajkovi.add(request.user)
        lajkovano=True

    return HttpResponseRedirect(reverse('detaljna', args=[str(pk)]))



def lajkuj_komentar(request, komentpk, objectpk):
    # id komentara
    id_komentara=komentpk
    # id posta
    print('pk='+str(komentpk))
    print('id='+str(objectpk))
    lajkovano_koment = False
    k = get_object_or_404(Komentari, id=int(komentpk))
    if k.lajkovi_za_koment.filter(id=request.user.id).exists():
        k.lajkovi_za_koment.remove(request.user)
        lajkovano_koment=False
        messages.success(request,"Odjavili ste vas glas za komentar.")
    else:
        k.lajkovi_za_koment.add(request.user)
        messages.success(request, "Vas glas je zabelezen.")
        lajkovano_koment=True
    #ul=ukupno_lajkova_za_komentar(request,komentpk,objectpk)
    #print("ul="+str(ul))
    #request.session['ul']=str(ul)
    return HttpResponseRedirect(reverse('detaljna', args=[str(objectpk)]))


def ukupno_lajkova_za_komentar_2(request, komentpk, objectpk):
    #return HttpResponse("LAJKOVANJE KOMENTARA")
    # treba da saznamo koliko je ukupno lajkova za komentar
    # https://stackoverflow.com/questions/5439901/getting-a-count-of-objects-in-a-queryset-in-django
    k = get_object_or_404(Komentari, id=int(komentpk))
    print("K="+str(k))
    #izdvoj iz tabele blog1_lajkovi_za_komentare sve zapise koji odgovaraju datom komentaru
    # prebroj ih
    #raw_query="SELECT * FROM blog1_komentari_lajkovi_za_koment WHERE komentari_id='"+str(komentpk)+"'"
    raw_query="SELECT COUNT(*) FROM blog1_komentari_lajkovi_za_koment WHERE komentari_id ='"+str(komentpk)+"'"
    c1=connection.cursor()
    c1.execute(raw_query)
    row = c1.fetchone()
    #c1.fetchall()
    print("c1=" + str(c1))
    print("row="+str(row))
    x=(str(row)).rstrip(",)")
    x=x.lstrip("(")
    print(str(x))
    return x
















class PocetniView(ListView):
    model = Postovi
    template_name = 'blog1/pocetna.html'
    # sortiracu postove da se prikazuju
    # od najmladjeg ka najstarijem
    ordering = ['-datum']
    # necu da stranku opterecujem sa puno postova
    # podelicu ih na po pet po stranici:
    paginate_by = 5



class ArticleDetailView(DetailView):
    model = Postovi
    template_name = 'blog1/detaljna.html'

    def get_context_data(self, *args, **kwargs):
        kateg_meni=Kategorija.objects.all()
        context=super(ArticleDetailView, self).get_context_data()

        x = get_object_or_404(Postovi, id=self.kwargs['pk'])
        ul = x.ukupno_lajkova()
        lajkovano=False
        if x.lajkovi.filter(id=self.request.user.id).exists():
            lajkovano=True

        context['kateg_meni'] = kateg_meni
        context['ukupno_lajkova']=ul
        context['lajkovano']=lajkovano
        return context

class KomentarDetailView(DetailView):
    model = Komentari
    template_name = 'blog1/detaljna.html'

    def get_context_data(self, *args, **kwargs):
        context=super(KomentarDetailView, self).get_context_data()
        x1=get_object_or_404(Komentari, id=self.kwargs['pk'])
        ul=x1.ukupno_lajkova_za_komentar()
        lajkovano1=False
        if x1.lajkovi_za_koment.filter(id=self.request.user.id).exists():
            lajkovano1=True
        context['ukupno_lajkova_za_komentar']=ul
        context['lajkovano1']=lajkovano1
        return context





class NoviPostView(CreateView):
    model = Postovi
    # Day 5
    form_class =PostForm
    template_name = 'blog1/novi_post.html'
    #Day 5
    #fields = "__all__" - ovo koristimo kad hocemo da prikazemo sva raspoloziva polja
    success_url = reverse_lazy('pocetna')

class AzurirajPostView(UpdateView):
    model = Postovi
    form_class = AzurirajPostForm
    template_name = 'blog1/azuriraj_post.html'
    #fields = ['naslov','naslov_tag','sadrzaj']
    success_url = reverse_lazy('pocetna')

class ObrisiPostView(DeleteView):
    model = Postovi
    template_name = 'blog1/obrisi_post.html'
    success_url = reverse_lazy('pocetna')

class NovaKategorija(CreateView):
    model=Kategorija
    template_name = 'blog1/nova_kategorija.html'
    fields = '__all__'

def KategorijaView(request, kateg):
    print(str(kateg))
    kategorisani_postovi=Postovi.objects.filter(kategorija=kateg.replace('-',' '))
    return render(request, 'blog1/kategorija.html',{'kateg_postovi':kategorisani_postovi,
                                                    'kategorija':kateg.title(),
                                                    })

def prikazi_spisak_kategorija(request):
    kategorije=Kategorija.objects.all()
    return render(request, 'blog1/kategorije_spisak.html',{'kateg_spisak':kategorije,
                                                           })


class NoviKomentarView(CreateView):
    model = Komentari
    #form_class = PostForm
    #fields = '__all__'
    form_class = KomentarForm
    template_name = 'blog1/novi_komentar.html'
    success_url = reverse_lazy('pocetna')

def dodaj_komentar_view_2(request, pk, user):
    prosledjeno=False
    if request.method=="POST":
        print('metod je POST')
        print('User='+str(user))
        print('pk='+str(pk))

        f=KomentarForm(request.POST)
        sadrzaj=request.POST['sadrzaj']
        ime_komentatora=str(user)
        print(str(sadrzaj))
        if f.is_valid():
            print('forma je validna')
            novi_komentar=f.save(commit=False)
            print('forma je na cekanju')
            novi_komentar.ime_komentatora=ime_komentatora
            novi_komentar.post_id=pk

            print(str(novi_komentar.post_id))
            novi_komentar.save()
            print('forma je snimljena')
            prosledjeno=True
            messages.success(request, "Vas komentar je uspesno dodat.")
            return redirect('detaljna', int(pk))
        else:
            messages.success(request, "Ups! Forma nije validna!")
            return HttpResponse("FORMA NIJE VALIDNA !")

    else:
        f = KomentarForm
        print('metod nije post')
        return render(request, 'blog1/novi_komentar.html', {'form': f,
                                                            'prosledjeno': prosledjeno,
                                                            'post_id': pk,
                                                            })




def pretraga_postova(request):
    if request.method=="POST":  # POST mora velikim slovima - case sensitive!
        print('metod je POST')
        s=request.POST['searched1']
        #x=request.GET['user_id']
        #print(str(x))
        print('s='+s)
        #rez_1 = Postovi.objects.filter(naslov__contains=str(s))
        #rez_1 = Postovi.objects.filter(naslov_tag__contains=str(s))
        #rez_2=Postovi.objects.filter(autor__contains=s)
        rez_2=Postovi.objects.filter(kategorija__contains=str(s))   # case sensitive ! - pazi kad popunjavas polje na formi
        rez_3=Postovi.objects.filter(sadrzaj__contains=str(s))

        rez_4=Postovi.objects.filter(naslov__contains=str(s))
        # hajde sada da pribavimo sve postove koje je napravio autor koji ima korisnicko ime <username>
        # polje username ne postoji u modelu Postovi, vec samo autor_id. Dakle, username autora moramo da ga pribavimo iz druge tabele.
        # gde ga imamo? imamo ga u tabeli User. ako iz modela User koji u sebi sadrzi zapis koji ima
        # odgovarajuce korisnicko ime, mozemo pribaviti vrednost polja <id> pomocu kojeg mozemo da saznamo i <autor_id>.
        # hajde prvo da pribavimo odgovarajuci zapis iz modela User. Nazvacemo ga 'x':
        try:
            x=User.objects.get(username=str(s))
            # promenljivoj x_id dodelicimo vrednost polja 'id' iz zapisa 'x':
            x_id=x.id
            # provericemo njegovu vrednost:
            print(str(x))
            # sada kad nam je poznat 'id', pomocu njega cemo potraziti odgovarajuci zapis iz modela 'Postovi':
            # U starmo SQL-u ovo bi moglo da se prevede kao 'SELECT * FROM Postovi WHERE autor_id=x_id:
            y=Postovi.objects.filter(autor_id=int(x_id))
            #sada promenljivu y koja u sebi sadrzi sve postove koje je kreirao <autor_id> mozemo
            # da predamo html podlozi.
        except:
            x=None
            y=None



        # Problem: ako trazena vrednost ne postoji, aplikacija ce vratiti gresku.

        # https://stackoverflow.com/questions/53356353/multiple-queries-in-django-orm
        rez_ukupno=rez_3|rez_4|rez_2
        rez_bez_duplikata=rez_ukupno.distinct()
        return render(request, 'blog1/pretraga_postova.html',{'trazeno':s,
                                                              'rezultat':rez_bez_duplikata,
                                                                'x':x,
                                                                'y':y,
                                                              })
    else:
        print('metod nije POST')
        return render(request, 'blog1/pretraga_postova.html', {})
