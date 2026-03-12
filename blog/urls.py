from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    #for this url, when we hope to see the detailed post, we should input the post_id as parameter
    #to identify the post we want to see.
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('dashboard/', views.dashboard, name='dashboard'),
]