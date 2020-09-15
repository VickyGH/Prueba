from django.urls import path

from . import views
from .views import *

#app_name = 'page'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login', views.Login),
    path('logout', views.Logout),

    # Client
    path('client', ClientView.as_view(),name = 'client'),
    path('client/edit/<int:pk>', Edit_ClientView.as_view(),name = 'client_edit'),

    # Provider
    path('provider/add', Add_ProviderView.as_view(), name='provider_add'),
    path('provider', ProviderView.as_view(), name='provider'),
    path('provider/edit/<int:pk>', Edit_ProviderView.as_view(), name='provider_edit'),
    path('provider/del/<int:pk>', Delete_ProviderView.as_view(), name='provider_del'),

    # Product
    path('product/add', Add_ProductView.as_view(), name='product_add'),
    path('product', ProductView.as_view(), name='product'),
    path('product/edit/<int:pk>', Edit_ProductView.as_view(), name='product_edit'),
    path('product/del/<int:pk>', Delete_ProductView.as_view(), name='product_del'),

    # Order
    path('order/add', Add_OrderView.as_view(), name='order_add'),
    path('order', OrderView.as_view(), name='order'),
    path('order/detail/<int:pk>', Detail_OrderView.as_view(), name='order_detail'),
    path('order/edit/<int:pk>', Edit_OrderView.as_view(), name='order_edit'),
    path('order/del/<int:pk>', Delete_OrderView.as_view(), name='order_del'),




]
