from django import forms
from .models import Item

Input_Classes=''
class NewItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ('name','description','interns','duration','category')


class EditItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ('name','description','interns','duration','category')

