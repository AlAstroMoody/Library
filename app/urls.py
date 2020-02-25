from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.Homepage.as_view(), name='index_url'),
    path('create/',
         views.BookCreate.as_view(), name='book_create_url'),
    path('library/', views.Library.as_view(), name='library_url'),
    path('catalog/', views.Catalog.as_view(), name='catalog_url'),
    path('<str:slug>/update/',
         views.BookUpdate.as_view(), name='book_update_url'),
    path('<str:slug>/delete/',
         views.BookDelete.as_view(), name='book_delete_url'),
    path('<str:slug>/', views.BookDetails.as_view(),
         name='book_details_url'),

]
