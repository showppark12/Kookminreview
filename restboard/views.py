from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .form import BlogForm
# Create your views here.

def list(request):
    blogs = Blog.objects.all()
    return render(request, 'list.html',{'blogs':blogs})

def detail(request,restboard_id):
    restboard = get_object_or_404(Blog, pk = restboard_id)
    return render(request, 'detail.html',{'restboard' :restboard})

def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('list')

    else: 
        form = BlogForm()
        return render(request, 'new.html', {'form':form})

def create(request):
    new_restboard = Blog()
    new_restboard.title = request.POST['title']
    new_restboard.pub_date = timezone.datetime.now()
    new_restboard.body = request.POST['body']
    new_restboard.save()
    return redirect('/restboard/'+str(new_restboard.id))

def edit(request,restboard_id):
    edit_restboard = get_object_or_404(Blog, pk = restboard_id)
    return render(request, 'edit.html',{'restboard':edit_restboard})

def update(request,restboard_id):
    update_restboard = get_object_or_404(Blog, pk = restboard_id)
    update_restboard.title = request.POST['title']
    update_restboard.pub_date = timezone.datetime.now()
    update_restboard.body = request.POST['body']
    update_restboard.save()
    return redirect('detail', update_restboard.id)

def delete(request,restboard_id):
    delete_restboard = get_object_or_404(Blog, pk = restboard_id)
    delete_restboard.delete()
    return redirect('list')