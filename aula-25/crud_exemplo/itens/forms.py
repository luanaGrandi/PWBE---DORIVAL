from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'  # ou pode passar a lista dos campos que gostaria ['nome', 'descricao']