from django import forms

from .models import Contest

# class ContestForm(forms.Form):
#     title = forms.CharField(label='Название', max_length=20)
#     description = forms.CharField(label='Описание', widget=forms.Textarea)
#     price = forms.IntegerField(label='Рекомендованная розничная цена', min_value=10, max_value=100)
#     comment = forms.CharField(label='Комментарий', widget=forms.Textarea, required=False)

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ('title', 'description', 'price', 'comment')