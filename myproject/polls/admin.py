from django.contrib import admin

from polls.models import Question, Choice

# Register your models here.
admin.site.register(Question) #모델 클래스를 주면 알아서 긁어서 admin site에 넣어준다
admin.site.register(Choice)