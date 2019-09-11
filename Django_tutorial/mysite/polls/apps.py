from django.apps import AppConfig

'''
앱을 현재의 프로젝트에 포함시키기 위해서는, 
앱의 구성 클래스에 대한 참조를 INSTALLED_APPS 설정에 추가해야 합니다. 
'''
class PollsConfig(AppConfig):
    name = 'polls'
