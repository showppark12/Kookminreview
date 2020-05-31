from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog,StudyComment
from django.utils import timezone
from .form import BlogForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'base/home.html', {"blogs":blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    comments = blog.comments.all()
    return render(request, 'base/detail.html',{'blog':blog, 'comments': comments})

def new(request):
    # 1. 데이터가 입력 된 후 제출 버튼을 누르고 데이터저장 =  post
    # 2.정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 = get
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            content = form.save(commit = False) # 임시저장 잠깐 보류
            content.pub_date = timezone.now()
            content.writer = request.user
            content.save()
            return redirect('studyboardhome')
    else:
        form = BlogForm()
        form.writer = request.user
        return render(request,'base/new.html',{'form':form})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.pub_date = timezone.datetime.now()
    new_blog.body= request.POST['body']
    new_blog.save()
    return redirect('/studyboard/'+str(new_blog.id))

def edit(request,blog_id):
    edit_blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'base/edit.html',{'blog':edit_blog})

def update(request,blog_id):
    update_blog = get_object_or_404(Blog,pk = blog_id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.datetime.now()
    update_blog.body= request.POST['body']
    update_blog.save()
    return redirect('studyboarddetail',update_blog.id)

def delete(request,blog_id):
    delete_blog = get_object_or_404(Blog, pk = blog_id)
    delete_blog.delete()
    return redirect('studyboardhome')

def sccreate(request, b_id):
    if request.method == 'POST':
        new_comment = StudyComment()
        new_comment.writer = get_object_or_404(User, username=request.user)
        new_comment.board = get_object_or_404(Blog,pk = b_id)
        new_comment.modify_date = timezone.datetime.now()
        new_comment.text = request.POST['sctext']
        new_comment.save()
    return redirect('studyboarddetail', b_id)


def sdelete_comment(request, c_id):
    comment = get_object_or_404(StudyComment, pk=c_id)
    b_id = comment.board.id
    comment.delete()
    return redirect('studyboarddetail', b_id)

