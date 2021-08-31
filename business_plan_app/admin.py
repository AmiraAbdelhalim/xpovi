from django.contrib import admin
from .models import Question, UserAnswer, UserTrial
from django.contrib.admin import site


site.register(Question)
site.register(UserAnswer)
site.register(UserTrial)
