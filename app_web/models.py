from django.db import models
from django.template.defaultfilters import slugify
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django_quill.fields import QuillField

# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        abstract=True

# la classe Competences
class Competences(BaseModel):
    titre=models.CharField(max_length=200)
    pourcentage=models.IntegerField(null=True,blank=True)

    class Meta:
        verbose_name="Competences"

    def __str__(self) -> str:
        return self.titre

class Education(BaseModel):
    formation=models.CharField(max_length=100)
    ecole=models.CharField(max_length=100,blank=True,null=True)
    periode=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)

    class Meta:
        verbose_name="Education"

    def __str__(self) -> str:
        return self.formation

class Langue(BaseModel):
    titre=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)

    class Meta:
        verbose_name="Langue"

    def __str__(self) -> str:
        return self.titre

class Interet(BaseModel):
    titre=models.CharField(max_length=200)

    class Meta:
        verbose_name="Interet"

    def __str__(self) -> str:
        return self.titre

class Qualite(BaseModel):
    titre=models.CharField(max_length=200)

    class Meta:
        verbose_name="Qualite"

    def __str__(self) -> str:
        return self.titre

class Certification(BaseModel):
    titre=models.CharField(max_length=200)

    class Meta:
        verbose_name="Certification"

    def __str__(self) -> str:
        return self.titre

class CompetenceSuplementaire(BaseModel):
    titre=models.CharField(max_length=200)

    class Meta:
        verbose_name="CompetenceSuplementaire"

    def __str__(self) -> str:
        return self.titre

class Experience(BaseModel):
    post=models.CharField(max_length=200)
    entreprise=models.CharField(max_length=200)
    periode=models.CharField(max_length=200)
    description=QuillField(blank=True,null=True)
    lien=models.CharField(max_length=200,blank=True,null=True)

    class Meta:
        verbose_name="Experience"

    def __str__(self) -> str:
        return self.post

class Stage(BaseModel):
    titre=models.CharField(max_length=200)
    entreprise=models.CharField(max_length=200,blank=True,null=True)
    periode=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    site=models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name="Stage"

    def __str__(self) -> str:
        return self.titre

class FormationAttestee(BaseModel):
    titre=models.CharField(max_length=200)
    entreprise=models.CharField(max_length=200,blank=True,null=True)
    periode=models.CharField(max_length=200)
    description=QuillField(blank=True,null=True)
    site=models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name="FormationAttestee"

    def __str__(self) -> str:
        return self.titre

class Info(BaseModel):
    nom=models.CharField(max_length=200)
    email=models.EmailField(blank=True,null=True,max_length=200)
    phone=PhoneNumberField(null=True,blank=True,unique=True)
    specialite=models.CharField(max_length=200,null=True,blank=True)
    apropos = models.TextField(blank=True, null=True)
    resume = QuillField(blank=True, null=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    naissance=models.DateField(max_length=200,null=True,blank=True)
    experience=models.CharField(max_length=200,null=True,blank=True)
    grade=models.CharField(max_length=200,null=True,blank=True)
    disponibilite=models.CharField(max_length=200,null=True,blank=True)
    site=models.CharField(max_length=200,null=True,blank=True)
    photo=models.ImageField(upload_to='avatar',blank=True,null=True)
    photoc=models.ImageField(upload_to='avatar',blank=True,null=True)
    photo_bg=models.ImageField(upload_to='avatar_bg',blank=True,null=True)
    twitter=models.CharField(blank=True,null=True,max_length=200)
    youtube=models.CharField(blank=True,null=True,max_length=200)
    facebook=models.CharField(blank=True,null=True,max_length=200)
    instagram=models.CharField(blank=True,null=True,max_length=200)
    linkdin=models.CharField(blank=True,null=True,max_length=200)
    competence=models.TextField(blank=True,null=True,help_text="bref description")
    langue=models.TextField(blank=True,null=True,help_text="bref description")
    education=models.TextField(blank=True,null=True,help_text="bref description")
    portfolio=models.TextField(blank=True,null=True,help_text="bref description")
    experience=models.TextField(blank=True,null=True,help_text="bref description")
    temoignage=models.TextField(blank=True,null=True,help_text="bref description")
    contact=models.TextField(blank=True,null=True,help_text="bref description")
    cv=models.FileField(upload_to='cv',blank=True,null=True)

    class Meta:
        verbose_name="Info"

    def __str__(self) -> str:
        return self.nom

# la classe service
class Icone(BaseModel):
    titre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Icone"

    def __str__(self) -> str:
        return self.titre

# la classe service
class Service(BaseModel):
    titre = models.CharField(max_length=100)
    icone = models.ForeignKey(Icone, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='services', blank=True, null=True)

    class Meta:
        ordering = ['-updated']
        verbose_name = "Service"

    def __str__(self) -> str:
        return self.titre

class Temoignage(BaseModel):
    nom = models.CharField(max_length=200)
    contenu = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='temoignages', blank=True, null=True)
    specialite = models.CharField(max_length=200, blank=True, null=True, )
    status = models.BooleanField(default=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name_plural = 'Temoignages'

    def __str__(self) -> str:
        return self.nom

# Contact
class Contact(BaseModel):
    nom = models.CharField(blank=True, null=True, max_length=100, name='nom', verbose_name='Nom')
    email = models.EmailField(blank=True, null=True, max_length=100, name='email', verbose_name='Email')
    sujet = models.CharField(blank=True, null=True, max_length=100, name='sujet', verbose_name='Sujet')
    message = models.TextField(blank=True, null=True, verbose_name='Message', name='message')

    class Meta:
        ordering = ['-updated']
        verbose_name = "Contact"

    def __str__(self) -> str:
        return self.nom
    
# la classe portofilio
class Portfolio(BaseModel):
    CHOIX_CATEGORIE=(
        ('filter-app','Securité'),
        ('filter-card', 'Desktop'),
        ('filter-web', 'Web'),
    )
    titre=models.CharField(max_length=100)
    url=models.URLField(blank=True,null=True,max_length=100,help_text="lien complet du site")
    lien=models.URLField(blank=True,null=True,max_length=100,help_text="lien github")
    description=models.TextField(blank=True,null=True,max_length=1000)
    image=models.ImageField(upload_to='Portfolios_images',blank=True,null=True)
    categorie=models.CharField(choices=CHOIX_CATEGORIE,default="first",max_length=100,blank=True,null=True)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name="Portfolio"

    def __str__(self) -> str:
        return self.titre

