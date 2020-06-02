lsfrom django.shortcuts import render, redirect, get_object_or_404
from .models import FoodBoard, FoodComment
from .form import FoodForm
from django.utils import timezone
from django.contrib.auth.models import User 


def FBoardHome(request):
    reviews = FoodBoard.objects.all()
    return render(request, "FBoardHome.html", { 'reviews': reviews })


def FBoardDetail(request, review_id):
    review = get_object_or_404(FoodBoard, pk=review_id)
    comments= review.comments.all()
    return render(request, 'FBoardDetail.html', { 'review': review, 'comments': comments })


def FBoardNew(request):
    #1, 데이터가 입력된 후 제출 버튼을 누르면 데이터 저장 -> post 방식
    #2. 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 -> get 방식
    if request.method == 'GET':
        form = FoodForm()
        form.writer = request.user
        return render(request, 'FBoardNew.html', { 'form': form })
    else:
        form = FoodForm(request.POST, request.FILES)
        # 입력 데이터 유효성 검사 해주기
        if form.is_valid():
            content = form.save(commit=False) #데이터 임시 저장(이후 살 붙이고 제대로 저장)
            content.pub_date = timezone.now()
            content.writer = request.user
            content.save()
            return redirect('food_home')


def FBoardEdit(request, review_id):
    edit_review = FoodBoard.objects.get(id= review_id)
    if request.method == 'GET':
        form = edit_review
    else:
        edit_review.title = request.POST['title']
        edit_review.img = request.FILES['img']
        edit_review.text = request.POST['text']
        edit_review.pub_date = timezone.now()
        edit_review.writer = request.user
        edit_review.save()
        return redirect('food_home')
    return render(request, 'FBoardEdit.html', {'form': form })


def FBoardDelete(request, review_id):
    to_be_deleted = get_object_or_404(FoodBoard, pk=review_id)
    to_be_deleted.delete()
    return redirect('food_home')


def new_comment(request, review_id):
    if request.method == 'POST':
        new_comment = FoodComment()
        new_comment.writer = get_object_or_404(User, username=request.user)
        new_comment.board = get_object_or_404(FoodBoard, pk = review_id)
        new_comment.pub_date = timezone.datetime.now()
        new_comment.text = request.POST['text']
        new_comment.save()
    return redirect('FBoardDetail', review_id)

def delete_comment(request, comment_id):
    del_comment = get_object_or_404(FoodComment, pk = comment_id)
    review_id = del_comment.board.id
    del_comment.delete()
    return redirect('FBoardDetail', review_id)