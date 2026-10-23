from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['name', 'product', 'document', 'start_date', 'end_date', 'cost']
