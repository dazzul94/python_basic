from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

# from django.template import loader
# from django.http import Http404

from .models import Question, Choice

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self): # 컨텍스트 오버라이딩
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    logger.debug('vote().question.id = {}'.format(question_id))
    # return HttpResponse("You're voting on question %s" %question_id)
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 콤마 빼면 에러남
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

'''
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
    } # context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값입니다.
    print(request)
    return HttpResponse(template.render(context, request))

    # 4. index.html 리턴 shortcut
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # 1. 스트링 리턴
    # return HttpResponse("You're looking at question %s." %question_id)
    # 2. 객체가 없을때 404 에러
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    # 3. 객체가 없을때 404 에러 shortcut
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response %question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s" %question_id)
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 콤마 빼면 에러남
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''