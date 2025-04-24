from django import forms
from .models import Post, Tag
from django.utils.text import slugify

class PostForm(forms.ModelForm):
    tags_str = forms.CharField(
        label='태그',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '태그를 쉼표(,)로 구분하여 입력해주세요. (예: Django, Python, 웹개발)'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'tags_str', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '이미지',
            'is_published': '공개 여부'
        }

    def save(self, commit=True):
        post = super().save(commit=False)
        
        if commit:
            post.save()
            
            # 기존 태그 제거
            post.tags.clear()
            
            # 새로운 태그 추가
            tag_names = [tag.strip() for tag in self.cleaned_data['tags_str'].split(',') if tag.strip()]
            for tag_name in tag_names:
                tag_slug = slugify(tag_name, allow_unicode=True)
                tag, created = Tag.objects.get_or_create(
                    name=tag_name,
                    defaults={'slug': tag_slug}
                )
                post.tags.add(tag)
        
        return post

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['tags_str'] = ', '.join(tag.name for tag in self.instance.tags.all()) 