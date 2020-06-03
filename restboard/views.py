from django.shortcuts import render, redirect, get_object_or_404
from .models import RestBoard,RestBoardComment
from .forms import RestBoardForm
from django.utils import timezone
from django.contrib.auth.models import User



# 게시글 crud

def rlist(request):
    rlist = RestBoard.objects.all()
    return render(request, "ha/rlist.html", {'rlist': rlist})


def rdetail(request, r_id):
    if request.user.is_authenticated:
        rdetail = get_object_or_404(RestBoard, pk=r_id)
        comments = rdetail.comments.all()
        return render(request, 'ha/rdetail.html', {'rdetail': rdetail, 'comments':comments})
    return redirect('login')

def rcreate(request):
    if request.method == 'POST':
        form = RestBoardForm(request.POST, request.FILES)
        if form.is_valid():
            RestBoard = form.save(commit=False)
            RestBoard.writer = request.user
            RestBoard.pub_date = timezone.now()
            RestBoard.save()
            return redirect('rlist')
    else:
        form = RestBoardForm()
        return render(request, 'ha/rcreate.html',{'form':form})

def rupdate(request, r_id):
    update_r = RestBoard.objects.get(id=r_id)
    if request.method == 'POST':
        form = RestBoardForm(request.POST, instance= update_r)
        if form.is_valid():
            form.save()
        return redirect('rdetail',r_id)
    else:
        form = RestBoardForm(instance= update_r)

    return render(request, 'ha/rupdate.html', {'form':form,'r':update_r})

def rdelete(request, r_id):
    delete_r = get_object_or_404(RestBoard, pk=r_id)
    delete_r.delete()
    return redirect('rlist')


# 스크랩
def rscrap(request, r_id):
    rest = get_object_or_404(RestBoard, pk=r_id)
    rest.rscrap_users.add(request.user)
    return redirect('rdetail', r_id)

def rrscrap(request, r_id):
    rest = get_object_or_404(RestBoard, pk=r_id)
    rest.rscrap_users.remove(request.user)
    if request.method == 'POST':
        return redirect('scrap')
    return redirect('rdetail', r_id)


# 커멘트
def ccreate(request, r_id):
    if request.method == 'POST':
        new_comment = RestBoardComment()
        new_comment.writer = get_object_or_404(User, username=request.user)
        new_comment.board = get_object_or_404(RestBoard,pk = r_id)
        new_comment.pub_date = timezone.datetime.now()
        new_comment.text = request.POST['rtext']
        new_comment.save()
    return redirect('rdetail', r_id)

def delete_comment(request, c_id, r_id):
    delete_comment = RestBoardComment.objects.get(id = c_id)
    delete_comment.delete()
    return redirect('rdetail', r_id)
