from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo, Giornalista
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
# Create your views here.
from django.views.generic.list import ListView
"""
def home(request):
    a=""
    g=""
    for art in Articolo.objects.all():
        a+=(art.titolo+"<br>")

    for gio in Giornalista.objects.all():
        g+=(gio.nome+"<br>")
    response="Articolo:<br>"+a+"<br>Giornalisti:<br>"+g
    print(response)

    return HttpResponse("<h1>"+response+"</h1>")
"""




"""def home(request):
    a=[]
    g=[]
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    
    response=str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>"+response+"</h1>")"""

def home(request):
    articoli=Articolo.objects.all()
    giornalisti=Giornalista.objects.all()
    context={"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)

def articoloDetailView(request, pk):
    #articolo=Articolo.objects.get(pk=pk)
    articolo=get_object_or_404(Articolo, pk=pk)
    context={"articolo": articolo}
    return render(request, "articolo_detail.html", context)

class ArticoloDetailViewCB(DetailView):
    model=Articolo
    template_name="articolo_detail.html"

class ArticoloListView(ListView):
    
    model=Articolo
    template_name="lista_articoli.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["articoli"]=Articolo.objects.all()
        return context


class GiornalistaDetailViewCB(DetailView):

    model=Giornalista
    template_name="giornalista_detail.html"

class GiornalistaListView(ListView):

    model=Giornalista
    template_name="lista_giornalisti.html"

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        context["giornalisti"]=Giornalista.objects.all()
        return context