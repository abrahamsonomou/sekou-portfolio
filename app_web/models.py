from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# Contact
class Contact(models.Model):
    nom=models.CharField(blank=True,null=True,max_length=100,name='nom',verbose_name='Nom')
    email=models.EmailField(blank=True,null=True,max_length=100,name='email',verbose_name='Email')
    sujet=models.CharField(blank=True,null=True,max_length=100,name='sujet',verbose_name='Sujet')
    message=models.TextField(blank=True,null=True,verbose_name='Message',name='message')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Create date',name='created')
    
    class Meta:
        ordering=['-created']
        verbose_name="Contact"

    def __str__(self) -> str:
        return self.nom
    
class Competences(models.Model):
    titre=models.CharField(verbose_name='Titre',max_length=200)
    pourcentage=models.IntegerField(null=True,blank=True,verbose_name="Pourcentage")

    class Meta:
        verbose_name="Competences"

    def __str__(self) -> str:
        return self.titre
    
class Categorie(models.Model):
    nom_categorie=models.CharField(verbose_name='nom_categorie',max_length=200)

    class Meta:
        verbose_name="Categorie"

    def __str__(self) -> str:
        return self.nom_categorie
    
class Service(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(blank=True,null=True,max_length=200,verbose_name='Slug')
    description=models.TextField(blank=True,null=True,name="description",verbose_name="Description")
    image=models.ImageField(upload_to='services',blank=True,null=True,name="image",verbose_name='Image')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')

    class Meta:
        ordering=['-created']
        verbose_name="Service"

    def __str__(self) -> str:
        return self.titre
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)
        
class Portfolio(models.Model):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(blank=True,null=True,max_length=200,verbose_name='Slug')
    date_projet=models.DateField(blank=True,null=True,max_length=100,verbose_name='Date projet')
    url=models.URLField(blank=True,null=True,max_length=100,verbose_name='Url')
    client=models.CharField(blank=True,null=True,max_length=100,verbose_name='Client')
    description=models.TextField(blank=True,null=True,max_length=1000,verbose_name='Desc1')
    image=models.ImageField(upload_to='Portfolios_images',blank=True,null=True,name="image",verbose_name='Image')
    image1=models.ImageField(upload_to='Portfolios_images',blank=True,null=True,name="image1",verbose_name='Image1')
    image2=models.ImageField(upload_to='Portfolios_images',blank=True,null=True,name="image2",verbose_name='Image2')
    image3=models.ImageField(upload_to='Portfolios_images',blank=True,null=True,name="image3",verbose_name='Image3')
    categorie=models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_categorie',
                                verbose_name='Categorie')
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    status=models.BooleanField(default=False,verbose_name="Status")

    class Meta:
        ordering=['-created']
        verbose_name="Portfolio"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)