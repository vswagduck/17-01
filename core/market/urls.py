from django.urls import path, include
from . import views

urlpatterns = [
    path('cart/',views.CartGeneririCreateList.as_view()),
    path('cart/id',views.CartGenericRetriveUpdate.as_view()),
    path('category/',views.CategoryGenericCreateList.as_view()),
    path('category/<int:pk>',views.CategoryGenericRetriveUpdate.as_view()),
    path('export/product',views.ProductExport.as_view()),
    path('products/',views.ProductsCreate_list.as_view()),
    path('products/<int:pk>/', views.ProductsDDU.as_view()),
]
