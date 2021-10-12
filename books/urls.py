from django.urls import path
from books import views

urlpatterns = [
    path('book_list/',views.book_list,name="book_list"),
    path('book/<int:id>/',views.book_detail, name ='book_detail'),
    #path('blogsearchbar/',views.blogsearchbar, name="blogsearchbar"),
  
]