import datetime

from django.db import models
from django.utils import timezone
'''
Question 은 질문(question) 과 발행일(publication date) 을 위한 두개의 필드를 가집니다. 
Choice 는 선택지(choice) 와 표(vote) 계산을 위한 두개의 필드를 가집니다. 
각 Choice 모델은 Question 모델과 연관(associated) 됩니다.
'''
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        # timedelta = 두 날짜나 시간의 차이인 기간
        # timezone.now() - datetime.timedelta(days = 1) : 하루전 날짜를 의미
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text