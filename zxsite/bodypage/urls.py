from django.conf.urls import url,include
from . import views

urlpatterns = [
#----------------------------------------------分割线--------------------------------------------------
    #主页
    url(r'^index/',views.index,name='index'),
#----------------------------------------------分割线--------------------------------------------------
    #用户注册登录等
    url(r'^login/$',views.log_in,name='login'),
    url(r'^logout/',views.log_out,name='logout'),
    url(r'^register/',views.register,name='register'),

#----------------------------------------------分割线--------------------------------------------------
    #用户信息
    url(r'^user/(?P<user_id>[0-9]+)/$',views.userpage,name='userpage'),
    url(r'^user/settings/(?P<user_id>[0-9]+)',views.edit_user_info,name='edit_user_info'),
    #用户管理文章
    url(r'^user/article-manage/(?P<user_id>[0-9]+)',views.article_manage,name='article_manage'),
    url(r'^user/article-manage/edit/(?P<article_id>[0-9]+)',views.article_edit,name='article_edit'),
    url(r'^user/article-manage/newarticle/(?P<user_id>[0-9]+)',views.new_article,name='new_article'),
    url(r'^user/article-manage/delete/((?P<user_id>[0-9]+))',views.d_article,name='d_aticle'),
    #用户删除文章
    url(r'^user/article-manage/delete/(?P<article_id>[0-9]+)',views.delete_article,name='delete_article'),

#----------------------------------------------分割线--------------------------------------------------
    #文章信息
    url(r'^article/(?P<article_id>[0-9]+)',views.article_ins,name='article_ins'),
    #文章评论信息
    url(r'^article/comments/(?P<article_id>[0-9]+)',views.article_ins_comment,name='article_ins_comments'),
    #文章点赞
    url(r'^article/likes/(?P<article_id>[0-9]+)',views.handle_like),


#----------------------------------------------分割线--------------------------------------------------
    #TAG相关
    url(r'^tag/articles/(?P<tag_id>[0-9]+)',views.tag_article,name='tag_article')
]