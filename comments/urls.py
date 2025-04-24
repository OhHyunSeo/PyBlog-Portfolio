from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('post/<int:post_pk>/create/', views.comment_create, name='comment_create'),
    path('<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    path('<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
] 