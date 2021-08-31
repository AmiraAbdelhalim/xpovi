from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    SECTION_LIST = [
        ('s1', 'Section1'),
        ('s2', 'Section2')
    ]
    TYPE_LIST = [
        ('bool', 'boolean'),
        ('choice', 'choice'),
        ('num', 'number')
    ]
    question = models.CharField(max_length=255)
    section = models.CharField(max_length=10, choices=SECTION_LIST)
    # for the frontend to know the type of inputs they will use
    type = models.CharField(max_length=255, choices=TYPE_LIST, null=True)

    def __str__(self):
        return self.question


class UserTrial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_trial", null=True)
    trial_num = models.IntegerField(null=True, unique=True)

    def __str__(self):
        return f'{self.trial_num}'


class UserAnswer(models.Model):
    # FIXME when answer is a number validate number to be positive integer
    # FIXME models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)], blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answer")
    answer = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_answer", null=True)
    trial = models.ForeignKey(UserTrial, on_delete=models.CASCADE, related_name="trial_number", null=True)

    def __str__(self):
        return self.answer
