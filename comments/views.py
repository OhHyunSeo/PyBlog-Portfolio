from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Post
from .models import Comment
from .forms import CommentForm

@login_required
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, '댓글이 성공적으로 작성되었습니다.')
    return redirect('blog:post_detail', pk=post_pk)

@login_required
def comment_update(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('blog:post_detail', pk=comment.post.pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, '댓글이 성공적으로 수정되었습니다.')
            return redirect('blog:post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'comments/comment_form.html', {
        'form': form,
        'comment': comment
    })

@login_required
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    post_pk = comment.post.pk
    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
    else:
        comment.delete()
        messages.success(request, '댓글이 성공적으로 삭제되었습니다.')
    return redirect('blog:post_detail', pk=post_pk) 