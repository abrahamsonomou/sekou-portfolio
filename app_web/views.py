from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from .forms import *
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core import mail
from django.conf import settings

# Create your views here.
def index(request):

    form=ContactForm(request.POST)

    info= Info.objects.order_by('-updated')[:1]
    competences = Competences.objects.order_by('-updated')
    services = Service.objects.all()
    portfolios = Portfolio.objects.filter(status=True)[:8]
    educations = Education.objects.order_by('-updated')
    experiences = Experience.objects.order_by('-updated')
    stages = Stage.objects.order_by('-updated')
    formations = FormationAttestee.objects.order_by('-updated')
    competencesuplementaires = CompetenceSuplementaire.objects.order_by('-updated')
    temoignages = Temoignage.objects.filter(status=True)

    context={
            'portfolios':portfolios,
            'temoignages':temoignages,
            'services':services,
            'competences':competences,
            'competencesuplementaires':competencesuplementaires,
            'infos':info,
            'educations':educations,
            'experiences':experiences,
            'stages':stages,
            'formations':formations,
            'form':form,
            }

    return render(request,'pages/index.html',context)

def detail_projet(request,pk:int):
    try:
        portfolio=Portfolio.objects.get(pk=pk)
        context={
            'portfolio':portfolio,
        }
    except Portfolio.DoesNotExist:
        raise("Ce projet n'exist pas")
    return render(request,'pages/detail_portfolio.html',context)

def cv(request):
    return render(request,'pages/cv.html')

# gestion des erreurs
def handler403(request,exception):
    return render(request,'pages/403.html')

def handler404(request, exception):
    return render(request,'pages/404.html',status=404)

def handler500(request):
    return render(request,'pages/500.html')

def handler503(request,exception):
    return render(request,'pages/503.html')  

def contact(request):
    form=ContactForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect('index')     