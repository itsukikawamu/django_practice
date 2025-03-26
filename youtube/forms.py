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
