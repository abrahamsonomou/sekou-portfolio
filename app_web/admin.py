from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Competences)
class CompetenceAdmin(admin.ModelAdmin):
    list_display=('titre','pourcentage',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display=('formation','ecole','periode')

@admin.register(Langue)
class LangueAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(Interet)
class InteretAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(CompetenceSuplementaire)
class CompetenceSuplementaireAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(Qualite)
class QualiteAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=('post','entreprise','periode',)

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display=('titre','entreprise','periode',)

@admin.register(FormationAttestee)
class FormationAttesteeAdmin(admin.ModelAdmin):
    list_display=('titre','entreprise','periode',)

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display=('nom','specialite',)
    ordering=('nom',)
    search_field=('nom','specialite',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(Icone)
class IconeAdmin(admin.ModelAdmin):
    list_display=('titre',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','email','sujet','message','updated',)
    ordering=('nom',)
    search_field=('nom','email',)

@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display=('nom','updated',)
    ordering=('nom',)
    search_field=('nom',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=('titre',)
    list_filter=('titre',)

