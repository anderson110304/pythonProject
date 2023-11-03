from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_view),
    path('book_detail/<int:id>/', views.book_detail_view),
    path('book_list/', views.delete_book_post_view),
    path('book_list/<int:id>/delete/', views.drop_book_view),
    path('create_post_book/', views.create_book_post_view),
    path('add-comment/', views.create_book_view),
]
