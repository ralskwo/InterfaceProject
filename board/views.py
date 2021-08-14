from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


# board_list
def index(request) :
    #목록
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'board_list.html', context)


# board_detail
def detail(request, question_id) :
    #내용 출력
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'board_detail.html', context)


# board_detail
def answer_create(request, question_id) :
    #댓글 입력
    question = Question.objects.get(id=question_id)
    '''
    #입력받은 내용 DB에 생성
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now()) 
    #answer.save()  로도 가능
    '''
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now)
    return redirect('detail', question_id=question_id)


# myboard_create
def question_create(request) :
    print("question_create수행")
    #질문등록
    if request.method == 'POST' :
        title = request.POST.get('title')
        content = request.POST.get('content')
        create_date = timezone.now()
        user= request.user
        Result = Question(subject=title, content=content, create_date=create_date, user=user)
        Result.save()
        context = { "msg" : "저장 완료"  }
    else :
        context = None
    return render(request, 'myboard_create.html', context)
# Create your views here.
