from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('productName','productType', 'producer',)
        labels = {
            'productName':'product Name',
            'productType':'product Type',
        }
        
    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        self.fields['producer'].empty_label = "Select"
       


   
