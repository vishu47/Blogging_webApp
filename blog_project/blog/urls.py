from django.contrib import admin
from django.urls import path,include
from blog import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<str:username>',UserPostListView.as_view(),name='user_posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name= 'post_detail'),
    path('post/new/',PostCreateView.as_view(),name= 'post_create'),  #by convention it expect post_form.html
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name= 'post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name= 'post_delete'),
    path('about/',views.about,name='blog-about'),
]
