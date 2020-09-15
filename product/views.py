from django.shortcuts import render
from datetime import datetime
from django.db import connection
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login, logout as do_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView

from account.models import Client
from product.forms import MyAuthenticationForm, ProviderForm, ProductForm, OrderForm
from product.models import Provider, Product, Order


def Login(request):
    form = MyAuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "login.html", {'form': form})


def Logout(request):
    do_logout(request)
    return redirect('/')


class Index(LoginRequiredMixin,TemplateView):
    template_name = "admin/index.html"


class ClientView(LoginRequiredMixin,ListView):
    template_name = "admin/client.html"
    queryset = Client.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(ClientView, self).get_context_data(**kwargs)
        context['types'] = ['Normal','Plata','Oro','Platino']
        return context

    def post(self, request, *args, **kwargs):
        #data = request.POST.get('name')
        client = Client.objects.create(
            name = request.POST.get('name'),
            code = request.POST.get('code'),
            image = request.POST.get('image'),
            address = request.POST.get('address'),
            type = request.POST.get('type'),
        )

        return self.get(self, *args, **kwargs)


class Edit_ClientView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['name','code','address','type']
    success_url = reverse_lazy('client')


class ProviderView(LoginRequiredMixin,ListView):
    template_name = "admin/provider.html"
    model = Provider

class Add_ProviderView(LoginRequiredMixin, CreateView):
    template_name = 'admin/new_data.html'
    form_class = ProviderForm
    success_url = '/provider'

    def get_context_data(self, **kwargs):
        context = super(Add_ProviderView, self).get_context_data(**kwargs)
        context['tipos'] = 'Proveedor'
        return context

class Edit_ProviderView(UpdateView):
    template_name = 'admin/edit_data.html'
    model = Provider
    fields = ['name','address',]
    success_url = reverse_lazy('provider')

    def get_context_data(self, **kwargs):
        context = super(Edit_ProviderView, self).get_context_data(**kwargs)
        context['tipos'] = 'Proveedor'
        return context

class Delete_ProviderView(DeleteView):
    model = Product
    success_url = reverse_lazy('provider')


class ProductView(LoginRequiredMixin,ListView):
    template_name = "admin/product.html"
    model = Product

class Add_ProductView(LoginRequiredMixin, CreateView):
    template_name = 'admin/new_data.html'
    form_class = ProductForm
    success_url = '/product'

    def get_context_data(self, **kwargs):
        context = super(Add_ProductView, self).get_context_data(**kwargs)
        context['tipos'] = 'Producto'
        return context

class Edit_ProductView(UpdateView):
    template_name = 'admin/edit_data.html'
    model = Product
    fields = ['code','description','provider']
    success_url = reverse_lazy('product')

    def get_context_data(self, **kwargs):
        context = super(Edit_ProductView, self).get_context_data(**kwargs)
        context['tipos'] = 'Producto'
        return context

class Delete_ProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('product')


class OrderView(LoginRequiredMixin,ListView):
    template_name = "admin/order.html"
    model = Order

class Add_OrderView(LoginRequiredMixin, CreateView):
    template_name = 'admin/new_data.html'
    form_class = OrderForm
    success_url = '/order'

    def get_context_data(self, **kwargs):
        context = super(Add_OrderView, self).get_context_data(**kwargs)
        context['tipos'] = 'Orden'
        return context

class Edit_OrderView(UpdateView):
    template_name = 'admin/edit_data.html'
    model = Order
    fields = ['client','product','assortment',
              'urgent','type','warehouse',
              'reference','code','detail']

    success_url = reverse_lazy('order')

    def get_context_data(self, **kwargs):
        context = super(Edit_OrderView, self).get_context_data(**kwargs)
        context['tipos'] = 'Orden'
        return context

class Delete_OrderView(DeleteView):
    model = Order
    success_url = reverse_lazy('order')


class Detail_OrderView(DetailView):
    template_name = 'admin/detail_data.html'
    model = Order

