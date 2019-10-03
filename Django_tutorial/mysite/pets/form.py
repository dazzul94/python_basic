from django import forms

from .models import Pet

class PetForm(forms.ModelForm):
  class Meta:
    model = Pet
    fields = ['pet_name']  # pet_name 속성만 사용한다는 뜻이다