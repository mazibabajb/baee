from django.urls import path
from blog import views

urlpatterns = [
    path('blog_list/',views.Post_view,name="blog_list"),
    path('blog/<int:id>/',views.blog_detail, name ='blog_detail'),
    path('blogsearchbar/',views.blogsearchbar, name="blogsearchbar"),
  
]