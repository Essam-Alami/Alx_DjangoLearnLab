from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
                PostListView, 
                PostDetailView, 
                PostCreateView, 
                PostUpdateView, 
                PostDeleteView,
                CommentCreateView,
                CommentUpdateView,
                CommentDeleteView,
                search_posts,
                posts_by_tag,
                PostByTagListView
                    )




urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # Built-in login/logout views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    
    path('', PostListView.as_view(), name='post-list'),               # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),   # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),        # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post



    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),


    path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
