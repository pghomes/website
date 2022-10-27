from django.urls import path

from .views import ProductListView, ProductDetailView





urlpatterns = [

path('', ProductListView.as_view() , name='product_listing'),
path('<int:pk>/', ProductDetailView.as_view() , name='product_detail'),

]

