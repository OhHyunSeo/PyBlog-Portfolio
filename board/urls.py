from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # 게시판 목록 페이지
    path('free/', views.PostListView.as_view(category='free'), name='free_board'),
    path('qna/', views.PostListView.as_view(category='qna'), name='qna'),
    path('showcase/', views.PostListView.as_view(category='showcase'), name='showcase'),
    
    # 게시글 CRUD
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # 댓글
    path('post/<int:post_id>/comment/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
] 