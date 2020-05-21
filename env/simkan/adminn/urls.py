from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('harga/',views.harga),
    path('area/',views.area),
    path('jual/',views.jual),
    path('user/',views.user),
    # path('harga/<idd>/delete',views.harga_delete),
    # path('area/<idd>/delete/',views.area_delete),
    # path('harga/<idd>/update',views.harga_update),
    # path('area/<idd>/update/',views.area_update),
    # path('user/<idd>/update',views.user_update),
]
