from django.urls import path
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
from blog.apps import BlogApplicationConfig


app_name = BlogApplicationConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='create'),
    path('post/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='delete'),
]