
#importando produto de models
from .models import Produto
from django import forms


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        #apresenta todos os campos
        fields = '__all__'


