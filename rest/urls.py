from django.urls import path

from . import views
from .views import *

urlpatterns = [

    # Client
    #path('client', ClientView.as_view(),name = 'client'),
    #path('client/edit/<int:pk>', Edit_ClientView.as_view(),name = 'client_edit'),
    
    path('client/create', CreateClient.as_view(), name="create_Client"),
    path('client/update/<int:pk>', UpdateClient.as_view(), name="update_Client"),
    path('client/list', ListClient.as_view(), name="list_Client"),
    path('client/delete/<int:pk>', DeleteClient.as_view(), name="delete_Client"),
    path('client/get/<int:pk>', GetClient.as_view(), name="get_Client"),

    # # Provider
    # path('provider/add', Add_ProviderView.as_view(), name='provider_add'),
    # path('provider', ProviderView.as_view(), name='provider'),
    # path('provider/edit/<int:pk>', Edit_ProviderView.as_view(), name='provider_edit'),
    # path('provider/del/<int:pk>', Delete_ProviderView.as_view(), name='provider_del'),
    #
    # # Product
    # path('product/add', Add_ProductView.as_view(), name='product_add'),
    # path('product', ProductView.as_view(), name='product'),
    # path('product/edit/<int:pk>', Edit_ProductView.as_view(), name='product_edit'),
    # path('product/del/<int:pk>', Delete_ProductView.as_view(), name='product_del'),
    #
    # # Order
    # path('order/add', Add_OrderView.as_view(), name='order_add'),
    # path('order', OrderView.as_view(), name='order'),
    # path('order/edit/<int:pk>', Edit_OrderView.as_view(), name='order_edit'),
    # path('order/del/<int:pk>', Delete_OrderView.as_view(), name='order_del'),




]
