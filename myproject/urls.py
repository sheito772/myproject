from django.contrib import admin
from django.urls import path, include # include追加
# auth.viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views
from django.conf import settings
# staticを追加
from rest_framework import routers
from django.conf.urls.static import static
from ranking.views import UserViewSet, ScoreViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('score/', include(router.urls)),

    path('slide/', include('slide.urls')),

    path('aisatu/', include("aisatu.urls")),
    
    # photo.urlsへのURLパターン
    path('', include('myapp.urls')),
    
    # accounts.urlsへのURLパターン
    path('', include('accounts.urls')),
    
    # パスワードリセットのためのURLパターン
    # PasswordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載
    # パスワードリセット申し込みページ
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
           template_name = "password_reset.html"),
         name ='password_reset'),
    
    # メール送信完了ページ
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
           template_name = "password_reset_sent.html"),
         name ='password_reset_done'),
    
    # パスワードリセットページ
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
           template_name = "password_reset_form.html"),
         name ='password_reset_confirm'),
    
    # パスワードリセット完了ページ
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
           template_name = "password_reset_done.html"),
         name ='password_reset_complete'),
]

# urlpatternsにmediaフォルダーのURLパターンを追加
urlpatterns += static(
   # MEDIA_URL = '/media/'
  settings.MEDIA_URL,
  # MEDIA_ROOTにリダイレクト
  document_root=settings.MEDIA_ROOT
  )