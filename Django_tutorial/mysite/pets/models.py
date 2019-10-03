from django.db import models
import os
# import settings

# Create your models here.
class Pet(models.Model):
  def __str__(self):
        return self.pet_name
  # 추후에 로그인 추가
  # owner = models.ForeignKey(User, on_delete=models.CASCADE)
  pet_name = models.CharField(max_length=100)
  image_path = models.ImageField(blank=True, null=True)

# No module named 'settings'
'''
  # delete 오버라이딩(정보를 지울 때 파일까지 지운다.)
  def delete(self, *args, **kargs):
      os.remove(os.path.join(settings.MEDIA_ROOT, self.image_path.path))
      super(Pet, self).delete(*args, **kargs) # 원래의 delete 함수를 실행
'''