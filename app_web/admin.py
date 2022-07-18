from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('titre','slug','created',)
    list_filter=('titre',)
    prepopulated_fields={'slug':('titre',)}
    
@admin.register(Competences)
class CompetenceAdmin(admin.ModelAdmin):
    list_display=('titre','pourcentage',)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('nom_categorie',)
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','email','sujet','message','created',)
    list_filter=('nom','email',)
    ordering=('nom',)
    
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=('titre','categorie','date_projet','url','client','created')
    list_filter=('titre','categorie',)
    prepopulated_fields={'slug':('titre',)}