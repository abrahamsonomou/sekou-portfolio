from django.shortcuts import render
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
    competences=Competences.objects.all()
    services=Service.objects.all()
    categories=Categorie.objects.all()
    object_list=Portfolio.objects.all()

    paginator=Paginator(object_list,6)
    page=request.GET.get('page')
    try:
        portfolios=paginator.page(page)
    except PageNotAnInteger:
        portfolios=paginator.page(1)
    except EmptyPage:
        portfolios=paginator.page(paginator.num_pages)
    
    context={
            'portfolios':portfolios,
            'page':page,
            'services':services,
            'competences':competences,
            'categories':categories,
            }
    return render(request,'pages/index.html',context)

def detail_projet(request,slug:str):
    try:
        portfolio=Portfolio.objects.get(slug=slug)
        context={
            'portfolio':portfolio,
        }
    except Portfolio.DoesNotExist:
        raise("Ce projet n'exist pas")
    return render(request,'pages/detail_portfolio.html',context)

class Contact(CreateView):
    model=Contact
    form_class=ContactForm
    template_name='pages/index.html'
    success_url='index'
    
# def contact(request):
#     form=ContactForm(request.POST)
#     if form.is_valid():
#         instance=form.save(commit=False)
#         if Contact.objects.filter(email=instance.email).exists():
#             messages.warning(request,
#             "Désolé! Cet email existe dans la base de données",
#             "alert alert-danger alert-dismissible")
#         else:
#             instance.save()
#             messages.success(request,
#             "Nous avons réçu votre message !",
#             "alert alert-success alert-dismissible")
#             connection = mail.get_connection()
#             nom=form.cleaned_data['nom']
#             email=form.cleaned_data['email']
#             sujet=form.cleaned_data['sujet']
#             message=form.cleaned_data['message']
#             email1 = mail.EmailMessage(
#             sujet,
#             message,
#             settings.DEFAULT_FROM_EMAIL,
#             [email],
#             connection=connection,
#             )
            
#             email1.send() 
            
#             connection.close()
            
#     context={
#         'form':form,
#         }
#     return render(request,"pages/index.html",context)
    # return render(request,"pages/newletter.html",context)
