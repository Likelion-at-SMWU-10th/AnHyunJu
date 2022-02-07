from django import forms
from .models import Blog

class BlogForm(forms.Form):
    #내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        #어떤 필드를 입력 받을건지
        #field = '__all__;
        fields = ['title','body']