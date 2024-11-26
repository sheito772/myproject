from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# django.views.genericからTemplateView、ListViewをインポート
from django.views.generic import TemplateView, ListView, FormView
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからPhotoPostFormをインポート
from .forms import PhotoPostForm, MailForm
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required
# modelsモジュールからモデルPhotoPostをインポート
from .models import MyPost
# django.views.genericからDetailViewをインポート
from django.views.generic import DetailView

from django.views.generic import DeleteView

from django.contrib import messages
from django.core.mail import EmailMessage

class IndexView(ListView):
    '''トップページのビュー
    '''
    # index.htmlをレンダリングする
    template_name ='toppage.html'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    queryset = MyPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 9

# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    '''写真投稿ページのビュー
    
    PhotoPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する
    
    Attributes:
      form_class: モデルとフィールドが登録されたフォームクラス
      template_name: レンダリングするテンプレート
      success_url: データベスへの登録完了後のリダイレクト先
    '''
    # forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    # レンダリングするテンプレート
    template_name = "post_photo.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
          form(django.forms.Form):
            form_classに格納されているPhotoPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
    '''
    # index.htmlをレンダリングする
    template_name ='post_success.html'

class CategoryView(ListView):
    '''カテゴリページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name ='toppage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、
      get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''     
      # self.kwargsでキーワードの辞書を取得し、
      # categoryキーの値(Categorysテーブルのid)を取得
      category_id = self.kwargs['category']
      # filter(フィールド名=id)で絞り込む
      categories = MyPost.objects.filter(
        category=category_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return categories

class UserView(ListView):
    '''ユーザーの投稿一覧ページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、
      get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''
      # self.kwargsでキーワードの辞書を取得し、
      # userキーの値(ユーザーテーブルのid)を取得
      user_id = self.kwargs['user']
      # filter(フィールド名=id)で絞り込む
      user_list = MyPost.objects.filter(
        user=user_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return user_list

class DetailView(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承する
     Attributes:
      template_name: レンダリングするテンプレート
      model: モデルのクラス
    '''
    # post.htmlをレンダリングする
    template_name ='detail.html'
    # クラス変数modelにモデルBlogPostを設定
    model = MyPost

class MypageView(ListView):
    '''マイページのビュー

    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.html をレンダリングする
    template_name = 'mypage.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = MyPost.objects.filter(
          user=self.request.user).order_by('-posted_at')
        return queryset

class PhotoDeleteView(DeleteView):
    model = MyPost
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('myapp:mypage')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
  
class MailView(FormView):
    '''お問い合わせページを表示するビュー

    フォームで入力されたデータを取得し、メールの作成を送信を行う
    '''
    # contact.htmlをレンダリングする
    template_name = 'mailform.html'
    # クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = MailForm
    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy('myapp:mail')

    def form_valid(self, form):
        '''FormViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したデータがPOSTしたときに呼ばれる
        メール送信を行う

        parameters:
            form(object): ContactFormのオブジェクト
        Return:
            HttpResponseRedirectのオブジェクト
            オブジェクトをインスタンス化するとsuccess_urlで
            設定されているURLにリダイレクトされる
        '''
        #フォームに入力されたデータをフィールド名を指定して取得
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        # メールのタイトルの書式を設定
        subject = 'お問い合わせ: {}'.format(title)
        # フォームの入力データの書式を設定
        message = '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}'.format(name, email, title, message)
        #
        from_email = 'tdn2430041@stu.o-hara.ac.jp'

        to_list = ['tdn2430041@stu.o-hara.ac.jp']

        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list)

        message.send()

        messages.success(self.request, 'お問い合わせは正常に送信されました。')

        return super().form_valid(form)