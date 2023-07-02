 # import form class from django
from dataclasses import field
from django import forms

from .models import Menu

class myForm(forms.ModelForm):

    # Text = forms.CharField(
    #     label=("Texto"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    # )

    class Meta:
        model = Menu
        fields = "text", "url_or_path", "font_awesome_icon", "new_tab",


        