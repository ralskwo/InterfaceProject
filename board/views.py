from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator

# board_list
def index(request) :
    #목록
    page = request.GET.get('page', 'detail/1')
    question_list = Question.objects.order_by('-create_date')

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    isUser = request.user.is_authenticated

    context = {'question_list': page_obj, 'isUser': isUser}
    return render(request, 'board_list.html', context)



# board_detail
def detail(request, question_id) :
    #내용 출력
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'board_detail.html', context)


# board_deta
def answer_create(request, question_id) :
    #댓글 입력
    question = Question.objects.get(id=question_id)

    comment_user = request.user
    print(comment_user)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now(),
                               comment_user=comment_user)
    return redirect('detail', question_id=question_id)


# myboard_create
def question_create(request):
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