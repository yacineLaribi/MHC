from django import forms
from .models import Item

Input_Classes=''
class NewItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ('name','description','interns','duration','category')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True

class EditItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ('name','description','interns','duration','category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True

