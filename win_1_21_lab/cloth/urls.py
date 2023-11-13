from django.urls import path
from . import views

urlpatterns = [
    path('cloth/product_list/', views.ProductListView.as_view(), name='product_list'),
    path('cloth/products/men/', views.men_cloth, name='men_cloth'),
    path('cloth/products/women/', views.women_cloth, name='women_cloth'),
    path('cloth/products/women/', views.kids_cloth, name='kids_cloth'),
    path('cloth/create_order/', views.CreateOrderView.as_view(),name='create_order'),
    path('cloth/products_by_tag/<str:tag_name>/', views.sort_products_by_tag, name='products_by_tag'),
    path('cloth/cloth_detail/<int:id>/', views.ClothDetailView.as_view(), name="cloth_detail"),
]
