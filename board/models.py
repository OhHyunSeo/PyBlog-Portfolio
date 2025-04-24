from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('free', '자유게시판'),
        ('qna', 'Q&A'),
        ('showcase', '웹사이트 자랑하기'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name='카테고리')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_posts', verbose_name='작성자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    image = models.ImageField(upload_to='board_images/', blank=True, null=True, verbose_name='이미지')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = '게시글'
        verbose_name_plural = '게시글 목록'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='게시글')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_comments', verbose_name='작성자')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    
    class Meta:
        ordering = ['created_at']
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'

    def __str__(self):
        return f'{self.author}의 댓글: {self.content[:20]}'
