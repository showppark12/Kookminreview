from django.shortcuts import render, redirect, get_object_or_404
from .models import BeerBoard, BeerBoardComment
from .forms import BeerBoardForm
from django.utils import timezone
from django.contrib.auth.models import User


def blist(request):
    blist = BeerBoard.objects.all()
    return render(request, "blist.html", {'blist': blist})


def bdetail(request, b_id):
    bdetail = get_object_or_404(BeerBoard, pk=b_id)
    comments= bdetail.comments.all()
    return render(request, 'bdetail.html', {'bdetail': bdetail, 'comments': comments})

def bcreate(request):
    if request.method == 'POST':
        form = BeerBoardForm(request.POST, request.FILES)
        if form.is_valid():
            beerboard = form.save(commit=False)
            beerboard.writer = request.user
            beerboard.pub_date = timezone.now()
            beerboard.save()
            return redirect('blist')
    else:
        form = BeerBoardForm()
        return render(request, 'bcreate.html',{'form':form})

def bupdate(request, b_id):
    update_b = BeerBoard.objects.get(id=b_id)
    if request.method == 'POST':
        form = BeerBoardForm(request.POST, instance= update_b)
        if form.is_valid():
            form.save()
        return redirect('bdetail',b_id)
    else:
        form = BeerBoardForm(instance= update_b)
        print("ㅎㅎ", form.as_p)

    return render(request, 'bupdate.html', {'form':form,'b':update_b})

def bdelete(request, b_id):
    delete_b = get_object_or_404(BeerBoard, pk=b_id)
    delete_b.delete()
    return redirect('blist')


def ccreate(request, b_id):
    if request.method == 'POST':
        new_comment = BeerBoardComment()
        new_comment.writer = get_object_or_404(User, username=request.user)
        new_comment.board = get_object_or_404(BeerBoard,pk = b_id)
        new_comment.pub_date = timezone.datetime.now()
        new_comment.text = request.POST['ctext']
        new_comment.save()
    return redirect('bdetail', b_id)


# def edit_comment(request, comment_id):
#     pass

def delete_comment(request, c_id):
    comment = get_object_or_404(BeerBoardComment, pk=c_id)
    b_id = comment.board.id
    comment.delete()
    return redirect('bdetail', b_id)