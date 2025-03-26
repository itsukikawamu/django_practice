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
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)