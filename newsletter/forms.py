from django.forms import ModelForm, TextInput, EmailInput, Form, IntegerField

from .models import Person


class NewsletterForm(ModelForm):
    class Meta:
        model = Person
        fields = ['email', 'nom']
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Email', 'required' : True}),
            'nom': TextInput(attrs={'placeholder': 'Nom', 'required' : True})
        }


class ReadForm(Form):
    person_id = IntegerField()
    mail_id = IntegerField()