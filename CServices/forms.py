from django import forms
from .models import WipReq

class WipForm(forms.ModelForm):

    class Meta:
        model = WipReq
        fields = ('name',
                  'size',
                  'bid',
                  'length',
                  'cost',
                  'meth'
                  )
