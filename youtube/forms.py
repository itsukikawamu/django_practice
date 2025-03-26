from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField(
        max_length=100, 
        required=False,
                widget=forms.TextInput(attrs={
            'placeholder': '検索',
            'class': 'form-control'
            })
        )

class ContactForm(forms.Form):
    name = forms.CharField(
        label='お名前', 
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    email = forms.EmailField(
        label='メールアドレス',
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }))
    message = forms.CharField(
        label='メッセージ', widget=forms.Textarea(attrs={
            'class': 'form-control'
        }))