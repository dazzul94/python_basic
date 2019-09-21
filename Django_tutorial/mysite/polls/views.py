from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 1. 스트링 리턴
    # return HttpResponse("Hello, world. You're at the polls index.")

    # 2. 텍스트로 리턴
    # output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    # 3. index.html 리턴
    template = loader.get_template('polls/index.html') # template 폴더에서 가져온다
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" %question_id)