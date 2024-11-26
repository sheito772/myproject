from django.forms import ModelForm
from .models import MyPost
from django import forms
from typing import Any, Mapping
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

class PhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = MyPost
        fields = ['category', 'title', 'comment', 'image1', 'image2','image3','image4']

class MailForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # nemeフィールドのplaceholderにメッセージを登録
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください'
        # nameフィールドを出力する
        self.fields['name'].widget.attrs['class'] = 'form-control'
        
        # emailフィールドのplaceholderにメッセージを登録
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        # emailフィールドを出力する<input>タグのclass属性を設定
        self.fields['email'].widget.attrs['class'] = 'form-control'

        # titleフィールドのplaceholderにメッセージを登録
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        # titleフィールドを出力する<input>タグのclass属性を設定
        self.fields['title'].widget.attrs['class'] = 'form-control'

        # massageフィールドのplaceholderにメッセージを登録
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください'
        # massageフィールドを出力する<input>タグのclass属性を設定
        self.fields['message'].widget.attrs['class'] = 'form-control'