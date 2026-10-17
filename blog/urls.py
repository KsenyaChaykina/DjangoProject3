from django.urls import path
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
from blog.apps import BlogApplicationConfig


app_name = BlogApplicationConfig.name

urlpatterns = [
    path('blog/', BlogPostListView.as_view(), name='list'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='detail'),
    path('blog/new/', BlogPostCreateView.as_view(), name='create'),
    path('blog/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='delete'),
]