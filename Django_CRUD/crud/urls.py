from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('pick_up_point/',views.pick_up_point,name="pick_up_point"),
    path('sort/',views.sort,name="sort"),
    path('create/', views.create, name='create' ),
    path('create_driver/', views.create_driver, name='create_driver' ),
    path('add_parcel/', views.add_parcel, name='add_parcel' ),
    path('add_driver/',views.add_driver,name="add_driver"),
    path('delete/<id>/', views.delete, name='delete' ),
    path('delete_driver/<id>/', views.delete_driver, name='delete_driver' ),
    path('edit/<id>/', views.edit, name='edit' ),
    path('edit_driver/<id>/', views.edit_driver, name='edit_driver' ),
    path('edit_sort/<id>/', views.edit_sort, name='edit_sort' ),
    path('update/<id>/', views.update, name='update' ),
    path('update_driver/<id>/', views.update_driver, name='update_driver' ),
    path('update_sort/<id>/', views.update_sort, name='update_sort' ),
    path('query/',views.query,name="query")

    ]
