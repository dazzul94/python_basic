from django.shortcuts import render
from .form import PetForm
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the pets index.")
'''   
def get_name(request):
    # POST로 폼데이터를 입력받을 때
    if request.method == 'POST':
        form = PetForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 유효성 검사 성공
            form.save()  # 저장해야 모델로 저장된다
            return HttpResponseRedirect('/Success/')

    # Get으로 받을 경우, 빈 Form을 템플릿에 출력한다
    else:
        form = PetForm()  # 빈 Form 생성
    return render(request, 'name.html', {'form': form})
'''
