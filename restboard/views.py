from django.shortcuts import render, redirect, get_object_or_404
from .models import RestBoard
from .forms import RestBoardForm
from django.utils import timezone
from django.contrib.auth.models import User


def rlist(request):
    rlist = RestBoard.objects.all()
    return render(request, "ha/rlist.html", {'rlist': rlist})


def rdetail(request, r_id):
    rdetail = get_object_or_404(RestBoard, pk=r_id)
    return render(request, 'ha/rdetail.html', {'rdetail': rdetail})

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


# def ccreate(request, b_id):
#     if request.method == 'POST':
#         new_comment = RestBoardComment()
#         new_comment.writer = get_object_or_404(User, username=request.user)
#         new_comment.board = get_object_or_404(RestBoard,pk = b_id)
#         new_comment.pub_date = timezone.datetime.now()
#         new_comment.text = request.POST['ctext']
#         new_comment.save()
#     return redirect('bdetail', b_id)


# def edit_comment(request, comment_id):
#     pass

# def delete_comment(request, comment_id):
#     pass