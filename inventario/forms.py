from django import forms
from .models import Productos

class FormProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'imagen', 'precio', 'stock', 'categoria_fk', 'origen']

        widgets = {
            'origen': forms.Select(choices=Productos.ORIGEN_CHOICES),
        }
