from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogsListView.as_view(), name='blogs-list'),
    path('bloggers/', views.BloggersListView.as_view(), name='bloggers-list'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(),
         name='blogger-detail'),
    path('blog/<int:pk>/create', views.add_comment, name='add-comment'),
    path('blog/create', views.add_blog, name='add-blog'),
]
