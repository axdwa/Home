from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('items/', views.item_list, name='item_list'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('items', views.items, name='items'),
]
