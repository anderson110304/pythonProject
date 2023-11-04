from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookView.as_view()),
    path('book_detail/<int:id>/', views.BookDetailView.as_view()),
    path('book_list/<int:id>/delete/', views.BookDropView.as_view()),
    path('book_list/<int:id>/update/', views.UpdateBookPostView.as_view()),
    path('create_book_post/', views.CreateBookPostView.as_view()),
    path('add-comment/', views.create_book_view),
    path('seacrh/', views.SearchView.as_view(), name='search'),
    #     path('', views.book_view),
    #     path('book_detail/<int:id>/', views.book_detail_view),
    #     path('book_list/', views.delete_book_post_view),
    #     path('book_list/<int:id>/delete/', views.drop_book_view),
    #     path('create_post_book/', views.create_book_post_view),
    #     path('add-comment/', views.create_book_view),
]
