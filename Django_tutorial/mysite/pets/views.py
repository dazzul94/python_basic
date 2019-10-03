from django.shortcuts import render
from .form import PetForm
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
from django.urls import reverse

# Create your views here.

def pet_form(request):
    # 추후에 user 추가
    # pet = Pet(owner=request.user)
    
    # POST로 폼데이터를 입력받을 때
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES) # user 추가
        # 유효성 검사
        if form.is_valid():
            # 유효성 검사 성공
            form.save()  # 저장해야 모델로 저장된다
            return HttpResponseRedirect(reverse('pets:results'))

    # Get으로 받을 경우, 빈 Form을 템플릿에 출력한다
    else:
        form = PetForm()  # 빈 Form 생성
    return render(request, 'pets/form.html', {'form': form})

def results(request):
    context = {'owner': 'suji'}
    return render(request, 'pets/results.html', context)
 
    

