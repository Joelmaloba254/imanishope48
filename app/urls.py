from django.urls import path
from . import views




urlpatterns = [
    path('base', views.base,name='base'),
    path('', views.homepage, name='homepage'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail')
]
