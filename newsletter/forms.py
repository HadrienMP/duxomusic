# -*-coding:utf-8-*-
from django.forms import ModelForm, TextInput, EmailInput, Form, IntegerField, FileField, ValidationError
import os

from .models import Person


def csv_only(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.csv']
    if ext not in valid_extensions or value.content_type != 'text/csv':
        raise ValidationError(u'Type de fichier non autorisé. Les types acceptés sont : CSV')


def required_cols(value):
    headers = enumerate(value).next()[1].replace('"', '').split(",")

    if 'name' not in headers and 'email' not in headers:
        raise ValidationError(u'Le fichier doit contenir au minimun les colonnes "email" et "name"')


class NewsletterForm(ModelForm):
    class Meta:
        model = Person
        fields = ['email', 'nom']
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Email', 'required': True}),
            'nom': TextInput(attrs={'placeholder': 'Nom', 'required': True})
        }


class ImportForm(Form):
    file = FileField(help_text="Fichier au format csv contenant les colonnes name, email, sign_up",
                     validators=[csv_only, required_cols])


class ReadForm(Form):
    person_id = IntegerField()
    mail_id = IntegerField()