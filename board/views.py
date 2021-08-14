from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator
from os import listdir

# board_list
def index(request) :
    full_name_main1 = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name1 = [name[:name.index('.')] for name in full_name_main1]

    #목록
    page = request.GET.get('page', 'detail/1')
    question_list = Question.objects.order_by('-create_date')

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    isUser = request.user.is_authenticated

    context = {'question_list': page_obj, 'isUser': isUser, 'princess_name1': princess_name1}
    return render(request, 'board_list.html', context)



# board_detail
def detail(request, question_id) :
    full_name_main1 = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name1 = [name[:name.index('.')] for name in full_name_main1]

    #내용 출력
    question = Question.objects.get(id=question_id)
    comment_user = request.user
    context = {'question': question, 'comment_user': comment_user, 'princess_name1': princess_name1}
    return render(request, 'board_detail.html', context)


# board_deta
def answer_create(request, question_id) :
    question = Question.objects.get(id=question_id)

    comment_user = request.user
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now(),
                               comment_user=comment_user)
    return redirect('detail', question_id=question_id)


# myboard_create
def question_create(request):
    full_name_main1 = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name1 = [name[:name.index('.')] for name in full_name_main1]

    #질문등록
    if request.method == 'POST' :
        title = request.POST.get('title')
        content = request.POST.get('content')
        create_date = timezone.now()
        user= request.user
        Result = Question(subject=title, content=content, create_date=create_date, user=user)
        Result.save()
        context = { "msg" : "저장 완료", "princess_name1": princess_name1}
    else :
        context = {"msg": None, "princess_name1": princess_name1}
    return render(request, 'myboard_create.html', context)

def delete_content(request):
    question_id = request.GET['id']
    writer = Question.objects.get(id=question_id)
    writer.delete()
    return redirect("index")

