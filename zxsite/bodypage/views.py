from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from .models import Article,Bloger,Comment,Tag,Subcomment
from django.contrib.auth.decorators import login_required
#----------------------------------------------分割线--------------------------------------------------
#主页视图函数
def index(request):
    articles = Article.objects.filter(status='P')
    tags = Tag.objects.order_by('related_articles')[:2]
    content = {
        'articles':articles,
        'tags':tags
    }
    return render(request,'bodypage/index.html',content)
#----------------------------------------------分割线--------------------------------------------------
#注册页处理函数
def register(request):
    if request.method == 'POST':
        #解包，获得3个值
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        #添加错误处理
        error = ''
        #检查重名
        name_check = User.objects.filter(username=username)
        if len(name_check) == 0:
            #检查密码是否相等
            if password1 == password2:
                ins_user = User.objects.create_user(
                    username = username,
                    password = password1
                )
                Bloger.objects.create(
                    user = ins_user
                )
                newuser = authenticate(username=username,password=password1)
                login(request,newuser)
                return redirect('/index')
            else:
                error = '密码重复，请重新注册'
                content = {
                    'errors':error
                }
                return render(request,'bodypage/register.html',content)
        else:
            error = '已存在相同用户名，请重新注册'
            content = {
                'errors':error
            }
            return render(request,'bodypage/register.html',content)

    else:
        return render(request, 'bodypage/register.html')
#----------------------------------------------分割线--------------------------------------------------
#登录处理函数
def log_in(request):
    print('adfadgfd')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            return redirect('/index')
        else:
            error = '用户不存在或者用户状态异常，请重新登录'
            content = {
                'errors':error
            }
            return render(request,'bodypage/login.html',content)
    else:
        print('sssssssss')
        return render(request,'bodypage/login.html')

#----------------------------------------------分割线--------------------------------------------------
#注销处理函数
def log_out(request):
    logout(request)
    return redirect('/index')
#----------------------------------------------分割线--------------------------------------------------
#用户主页函数
def userpage(request,user_id):
    #a = request.get_full_path() request.path
    #print(a)
    user_info = User.objects.get(id=user_id)
    user_info_profile = Bloger.objects.get(user=user_info)
    user_article = Article.objects.filter(author=user_info_profile).filter(status='P')
    user_comments = Comment.objects.filter(author=user_info_profile)
    user_subcomments = Subcomment.objects.filter(author=user_info_profile)

    content = {
        'user_info':user_info,
        'user_info_profile':user_info_profile,
        'user_article':user_article,
        'user_comments':user_comments,
        'user_subcomments':user_subcomments,
        'current_userid':user_id
    }

    return render(request,'bodypage/user.html',content)

#----------------------------------------------分割线--------------------------------------------------
#用户管理文章页面
def article_manage(request,user_id):
    user_ins = User.objects.get(id=user_id)
    user_ins_profile = Bloger.objects.get(user=user_ins)
    user_article = Article.objects.filter(author=user_ins_profile)
    user_article_P = user_article.filter(status='P')
    user_article_E = user_article.filter(status='E')
    user_article_D = user_article.filter(status='D')
    content = {
        'user_ins':user_ins,
        'user_ins_profile':user_ins_profile,
        'user_article_P':user_article_P,
        'user_article_E': user_article_E,
        'user_article_D': user_article_D,
    }
    return render(request,'bodypage/article_manage.html',content)
# ----------------------------------------------分割线--------------------------------------------------
#用户编辑自己的文章
def article_edit(request,article_id):
    if request.method == 'POST':
        print(request.POST)
        article = Article.objects.get(id=article_id)
        #user_id =request.POST.get('user_id')
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.status = request.POST.get('status')
        article.save()
        return redirect('/user/article-manage/1')

    else:
        article_instance = Article.objects.get(id=article_id)

        content = {
            'article_instance':article_instance
        }
        return render(request,'bodypage/edit-article.html',content)

# ----------------------------------------------分割线--------------------------------------------------
#用户删除文章
def delete_article(request,article_id):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        article_instance = Article.objects.get(id=article_id)
        article_instance.status = 'D'
        article_instance.save()
        return redirect('/user/article-manage/%s'%user_id)
# ----------------------------------------------分割线--------------------------------------------------
#用户文章回收站
def d_article(request,user_id):
    user_ins = User.objects.get(id=user_id)
    bloger_ins = Bloger.objects.get(user=user_ins)
    article_d = Article.objects.filter(author=bloger_ins).filter(status='D')
    print(article_d)
    content = {
        'articles':article_d
    }
    return render(request,'bodypage/delete_article.html',content)
# ----------------------------------------------分割线--------------------------------------------------
#用户个人信息编辑
def edit_user_info(request,user_id):
    if request.method == 'POST':
        user_firstname = request.POST.get('firstname')
        user_lastname = request.POST.get('lastname')
        user_email = request.POST.get('email')
        user_p_age = request.POST.get('age')
        user_p_gender = request.POST.get('gender')
        user_p_sig = request.POST.get('signiture')
        user_p_add = request.POST.get('address')
        User.objects.update(
            first_name = user_firstname,
            last_name = user_lastname,
            email = user_email
        )
        Bloger.objects.update(
            age = user_p_age,
            gender = user_p_gender,
            signiture = user_p_sig,
            address = user_p_add
        )
        return redirect('/user/%s'%user_id)
    else:
        user_info = User.objects.get(id=user_id)
        user_info_profile = Bloger.objects.get(user=user_info)
        content = {
            'user_info':user_info,
            'user_info_profile':user_info_profile
        }

        return render(request,'bodypage/edituserinfo.html',content)
#----------------------------------------------分割线--------------------------------------------------

#显示文章页面
def article_ins(request,article_id):
    article_instance = Article.objects.get(id=article_id)
    #浏览量的计数存在问题，应该朝着IP请求方面思考
    article_instance.views +=1
    article_instance.save()
    article_bloger = Bloger.objects.get(id=article_instance.author_id)
    article_user = User.objects.get(id=article_bloger.user_id)
    article_comment = Comment.objects.filter(article=article_instance)
    content = {
            'article_instance':article_instance,
            'article_bloger':article_bloger,
            'article_user':article_user,
            'article_comment':article_comment
        }

    return render(request,'bodypage/article_ins.html',content)
# ----------------------------------------------分割线--------------------------------------------------
@login_required(login_url='/login')
def handle_like(request,article_id):
    if request.method == 'POST':
        article_instance = Article.objects.get(id=article_id)
        article_instance.likes += 1
        article_instance.save()
        return redirect('/article/%s' % article_id)

#----------------------------------------------分割线--------------------------------------------------
#处理文章评论
@login_required(login_url='/login')
def article_ins_comment(request,article_id):
    if request.method == 'POST':
        print(request.POST)
        comment = request.POST.get('comment')
        comment_user_id = request.POST.get('blogerid')
        commenter = Bloger.objects.get(user_id=comment_user_id)

        #article_instance = Article.objects.get(id=article_id)
        Comment.objects.create(
            article_id = article_id,
            author = commenter,
            content = comment,
            status = 'P'
        )
        return redirect('/article/%s'%article_id)
    else:
        return redirect('/article/%s' % article_id)

#----------------------------------------------分割线--------------------------------------------------
#新建文章
def new_article(request,user_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        bloger = Bloger.objects.get(user_id=user_id)
        Article.objects.create(
            title = title,
            content = content,
            status = status,
            author = bloger
        )
        return redirect('/user/article-manage/%s'%user_id)
    else:

        return render(request,'bodypage/newarticle.html')


#----------------------------------------------分割线--------------------------------------------------
#从TAG到文章
def tag_article(request,tag_id):
    tags_all = Tag.objects.exclude(id=tag_id).order_by('related_articles')[:5]
    tag_ins = Tag.objects.get(id=tag_id)
    article_lists = Article.objects.filter(tags=tag_ins).filter(status='P')
    content = {
        'tag':tag_ins,
        'articles':article_lists,
        'tags_all':tags_all
    }
    return render(request,'bodypage/tag-article.html',content)