from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['lead', 'contract']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Предзаполняем поле lead, если передан initial
        if 'initial' in kwargs and 'lead' in kwargs['initial']:
            self.fields['lead'].initial = kwargs['initial']['lead']
            self.fields['lead'].widget.attrs['readonly'] = True
