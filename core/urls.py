from django.urls import path
from.views import index
from . import views

urlpatterns =[
    path('', index, name="index"),
    path('iniciar_sesion/', views.inicia_crea_sesion, name='inicia_crea_sesion'),
    path('lo_mas_vendido/', views.lo_mas_vendido, name='lo_mas_vendido'),
    path('', views.index_view, name='index'),
    path('carrito/', views.carrito, name='carrito'),
    path('new/', views.new, name='new'),
    path('halo_infinite_producto/', views.halo_infinite_producto, name='halo_infinite_producto'),
    path('halo_ce_producto/', views.halo_ce_producto, name='halo_ce_producto'),
    path('destiny_producto/', views.destiny_producto, name='destiny_producto'),
    path('FF7_producto/', views.FF7_producto, name='FF7_producto'),
    path('codmw2_producto/', views.codmw2_producto, name='codmw2_producto'),
    path('spiderman_producto/', views.spiderman_producto, name='spiderman_producto'),
    path('bf_2042_producto/', views.bf_2042_producto, name='bf_2042_producto'),
    path('elden_ring_producto/', views.elden_ring_producto, name='elden_ring_producto'),
    path('modificar_usuario/', views.modificar_usuario, name='modificar_usuario'),
    path("", views.index, name="index"),

  
  
 ]