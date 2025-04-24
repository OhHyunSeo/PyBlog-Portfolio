from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='이메일',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='아이디',
        help_text='150자 이하의 문자, 숫자, @/./+/-/_ 만 사용 가능합니다.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='<ul>'
                 '<li>비밀번호는 최소 8자 이상이어야 합니다.</li>'
                 '<li>비밀번호는 숫자만으로 이루어질 수 없습니다.</li>'
                 '<li>비밀번호는 일상적인 단어나 개인정보를 포함할 수 없습니다.</li>'
                 '<li>비밀번호는 너무 흔한 것이어서는 안됩니다.</li>'
                 '</ul>'
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='비밀번호를 다시 입력해주세요.'
    )
    profile_image = forms.ImageField(
        required=False,
        label='프로필 이미지',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    bio = forms.CharField(
        required=False,
        label='자기소개',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        help_text='자신을 소개하는 글을 작성해주세요.'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_image', 'bio')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'profile_image', 'bio', 'github_url']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'github_url': forms.URLInput(attrs={'placeholder': 'https://github.com/yourusername'})
        }

    def clean_github_url(self):
        url = self.cleaned_data.get('github_url')
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url 