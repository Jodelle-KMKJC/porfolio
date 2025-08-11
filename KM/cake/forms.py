from django import forms
from .models import Gateau

class GateauForm(forms.ModelForm):
    class Meta:
        model = Gateau
        fields = ['nom', 'description', 'prix', 'image', 'categorie', 'disponibilite', 'avis', 'is_deleted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border rounded'}),
            'avis': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border rounded'}),
            'nom': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'prix': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded', 'step': '0.01'}),
            'image': forms.FileInput(attrs={'class': 'w-full p-2 border rounded'}),
            'categorie': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'disponibilite': forms.CheckboxInput(attrs={'class': 'h-5 w-5'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        