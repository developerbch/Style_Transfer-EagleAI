"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path#, include
from illusion import views
# from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

# from . import backends

# router = routers.DefaultRouter()
# router.register(r'members', views.MemberViewSet)  # 회원정보 접근 url
# router.register(r'history', views.HistoryViewSet)  # history 접근 url
# router.register(r'timeline', views.TimelineViewSet)  # timeline 접근 url
# router.register(r'replies', views.ReplyViewSet)  # 댓글 접근 url
# router.register(r'styles', views.StyleViewSet)  # style_db 접근 url
# router.register(r'content-image', views.ContentImageViewSet)  # content-image 업로드 url

# router.register(r'preview', views.PreviewViewSet)

# router.register(r'transfer', 추가해라추가추가추가)  # transfer 작동 url
# router.register(r'test', backends.FirebaseBackend)

from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('signin/', views.signIn),
    # path('postsign/', views.postsign),
    # path('logout/', views.logout, name="log"),
    # path('signup/', views.signUp, name="signup"),
    # path('postsignup/', views.postsignup, name="postsignup"),
    # path('create/', views.create, name="create"),
    # path('post_create/', views.post_create, name="post_create"),
    # path('check/', views.check, name="check"),
    # path('post_check/', views.post_check, name="post_check"),

    # path('preview/<int:style_id>/<path:url>', views.preview),

    re_path(r'preview/(?P<style_id>[0-9]*)/(?P<url>.*)', views.preview), #물음표전까지는 받아짐
    re_path(r'transfer/(?P<style_id>[0-9]*)/(?P<url>.*)', views.transfer), #물음표전까지는 받아짐

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
