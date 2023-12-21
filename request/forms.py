from django import forms
from .models import NewRequestModel


class NewRequestForm(forms.ModelForm): 
    class Meta:
        model = NewRequestModel
        fields = ('name','email','major','phone','description','resume')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True

