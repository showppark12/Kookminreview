from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodBoard
from .form import FoodForm
from django.utils import timezone

def home(request):
    reviews = FoodBoard.objects.all()
    return render(request, "home.html", { 'reviews': reviews })


def detail(request, review_id):
    review = get_object_or_404(FoodBoard, pk=review_id)
    return render(request, 'detail.html', { 'review': review })


def new(request):
    #1, 데이터가 입력된 후 제출 버튼을 누르면 데이터 저장 -> post 방식
    #2. 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 -> get 방식
    if request.method == 'GET':
        form = FoodForm()
        return render(request, 'new.html', { 'form': form })
    else:
        form = FoodForm(request.POST, request.FILES)
        # 입력 데이터 유효성 검사 해주기
        if form.is_valid():
            content = form.save(commit=False) #데이터 임시 저장(이후 살 붙이고 제대로 저장)
            content.pub_date = timezone.now()
            content.save()
            return redirect('food_home')


def edit(request, review_id):
    edit_review = get_object_or_404(FoodBoard, pk=review_id)
    if request.method == 'GET':
        form = FoodForm(instance=edit_review)
    else:
        form = FoodForm(request.POST, request.FILES, instance=edit_review)
        # 입력 데이터 유효성 검사 해주기
        if form.is_valid():
            content = form.save(commit=False) #데이터 임시 저장(이후 살 붙이고 제대로 저장)
            content.pub_date = timezone.now()
            content.save()
            return redirect('detail', content.id)
    return render(request, 'edit.html', { 'form': form, 'id': edit_review.id })


def delete(request, review_id):
    to_be_deleted = get_object_or_404(FoodBoard, pk=review_id)
    to_be_deleted.delete()
    return redirect('food_home')