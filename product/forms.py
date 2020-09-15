from django import forms
from django.contrib.auth.forms import AuthenticationForm

from product.models import Provider, Product, Order


class MyAuthenticationForm(AuthenticationForm):
    # add your form widget here

    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)

        self.base_fields['username'].widget.attrs['class'] = 'form-control py-4'
        self.base_fields['username'].widget.attrs['id'] = 'inputEmailAddress'
        self.base_fields['username'].widget.attrs['type'] = 'email'
        self.base_fields['username'].widget.attrs['placeholder'] = 'Usuario'

        self.base_fields['password'].widget.attrs['class'] = 'form-control py-4'
        self.base_fields['password'].widget.attrs['id'] = 'inputPassword'
        self.base_fields['password'].widget.attrs['type'] = 'password'
        self.base_fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class ProviderForm(forms.ModelForm):
    class Meta:
            model = Provider
            exclude = ('created_at','updated_at','closed_at')

            widgets = {
                'name': forms.TextInput(attrs={
                    'type': "text",
                    'name': "name",
                    'class': "form-control",
                    'placeholder': "Nombre(s)*",
                }),
                'address': forms.Textarea(attrs={
                    'name': "address",
                    'class': "form-control",
                    'placeholder': "Dirección*",
                }),

            }

class ProductForm(forms.ModelForm):
    class Meta:
            model = Product
            exclude = ('created_at','updated_at','closed_at')


            widgets = {
                'code': forms.TextInput(attrs={
                    'type': "text",
                    'name': "code",
                    'class': "form-control",
                    'placeholder': "Nombre(s)*",
                }),
                'description': forms.Textarea(attrs={
                    'name': "description",
                    'class': "form-control",
                    'placeholder': "Descripción*",
                }),
                'provider':forms.SelectMultiple(attrs={
                        'name': "provider",
                        'class': "form-control",
                        'placeholder': "Proveedores*",
                }),
            }


class OrderForm(forms.ModelForm):

    class Meta:
            model = Order
            exclude = ('created_at','updated_at','closed_at')
            #
            # client = models.ForeignKey(Client, related_name='order_client', on_delete=models.SET_NULL, null=True)
            # product = models.ForeignKey(Product, related_name='order_product', on_delete=models.SET_NULL, null=True)
            # assortment = models.DateTimeField(auto_now=False, blank=True, null=True)
            # urgent = models.BooleanField(default=False)
            # type = models.CharField(max_length=100, blank=True, choices=Type_Choice, default='center_distribution')
            # warehouse = models.CharField(max_length=100, blank=True, null=True)
            # reference = models.CharField(max_length=100, blank=True, null=True)
            # code = models.IntegerField(blank=True, null=True)
            # detail = models.TextField()

            widgets = {
                'client': forms.Select(attrs={
                    #'type': "text",
                    'name': "client",
                    'class': "form-control",
                    'placeholder': "Cliente*",
                }),
                'product': forms.Select(attrs={
                    'name': "product",
                    'class': "form-control",
                    'placeholder': "Producto*",
                }),
                'assortment': forms.DateInput(attrs={
                    'name': "assortment",
                    'class': "form-control",
                    'placeholder': "Fecha de Surtido*",
                }),
                'urgent': forms.CheckboxInput(attrs={
                    'name': "urgent",
                    'class': "form-control",
                    'placeholder': "Urgente*",
                }),
                'type': forms.Select(attrs={
                    'name': "type",
                    'class': "form-control",
                    'placeholder': "Tipo*",
                }),
                'warehouse': forms.TextInput(attrs={
                    'name': "warehouse",
                    'class': "form-control",
                    'placeholder': "Almacen*",
                }),
                'reference': forms.TextInput(attrs={
                    'name': "reference",
                    'class': "form-control",
                    'placeholder': "Referencia*",
                }),
                'code': forms.TextInput(attrs={
                    'name': "code",
                    'class': "form-control",
                    'placeholder': "Codigo*",
                }),
                'detail': forms.Textarea(attrs={
                    'name': "detail",
                    'class': "form-control",
                    'placeholder': "Detalle de Pedido*",
                }),
            }

