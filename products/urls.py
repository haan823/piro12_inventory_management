from django.urls import path

from products.views import products_list, products_detail, products_registration, sellers_registration, sellers_list, \
    sellers_detail, products_remaining_plus, products_remaining_minus, products_modify, products_delete, sellers_modify, \
    sellers_delete

urlpatterns = [
    path('', products_list, name='products-list'),
    path('<int:pk>/', products_detail, name='products-detail'),
    path('products_registration/', products_registration, name='products-registration'),
    path('sellers_registration/', sellers_registration, name='sellers-registration'),
    path('sellers_list/', sellers_list, name='sellers-list'),
    path('sellers_list/<int:pk>/', sellers_detail, name='sellers-detail'),
    path('products_remaining_plus/<int:pk>/', products_remaining_plus, name='products-remaining-plus'),
    path('products_remaining_minus/<int:pk>/', products_remaining_minus, name='products-remaining-minus'),
    path('<int:pk>/modify/', products_modify, name='products-modify'),
    path('<int:pk>/delete/', products_delete, name='products-delete'),
    path('sellers_list/<int:pk>/modify/', sellers_modify, name='sellers-modify'),
    path('sellers_list/<int:pk>/delete/', sellers_delete, name='sellers-delete'),
]