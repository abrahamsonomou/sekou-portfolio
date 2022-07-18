from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['nom','email','message','sujet']
        labels={'nom':'Full Name','email':'Email Address','message':'Message','sujet':'Sujet'}
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control','placeholder':"Nom"}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':"Email"}),
            'sujet':forms.TextInput(attrs={'class':'rounded form-control mr-2 py-3','placeholder':"Sujet"}),
            'message':forms.Textarea(attrs={'class':'form-control','cols':30,'rows':10,'placeholder':"Message"})
        }
        
        