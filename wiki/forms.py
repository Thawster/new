from django import forms
from wiki.models import Page
from django.forms import ModelForm


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    model = Page
class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)