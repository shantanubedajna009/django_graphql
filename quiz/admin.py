from django.contrib import admin
from .models import Question,Quizzes,Answer,Category

# Register your models here.


admin.site.register(Question)
admin.site.register(Quizzes)
admin.site.register(Answer)
admin.site.register(Category)

