from django import forms
from .models import Contact, Comment
from django.utils.safestring import mark_safe

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'コメントする',
                'autocomplete': 'off',
                }),
        }

class SearchForm(forms.Form):
    keywords = forms.CharField(
        max_length=100, 
        required=False,
                widget=forms.TextInput(attrs={
            'placeholder': '検索',
            'class': 'form-control'
            })
        )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'お名前',
            'email': mark_safe('メールアドレス <span class="text-secondary">(任意)</span>'),
            'message': 'メッセージ',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': False,
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control'
                }),
        }