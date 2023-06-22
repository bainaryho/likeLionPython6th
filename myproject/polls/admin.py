from django.contrib import admin

from polls.models import Question, Choice


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] #filedset을 만들어 줌
    fieldsets = [  # 수동으로 커스터 마이징. fields랑 동시에 안씀
        ('Question Statemanet', {'fields': ['question_text']}),
        ('Date Infomation', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)  # 모델 클래스를 주면 알아서 긁어서 admin site에 넣어준다
admin.site.register(Choice)
