from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# class AnswerSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#
#     class Meta:
#         model = Answer
#         fields = ('id', 'answer',)
#         read_only_fields = ('id',)


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    question = serializers.CharField(required=False)

    class Meta:
        model = Question
        fields = ('id', 'question', 'type')
        read_only_fields = ('id',)


class AnswerSerializer(serializers.ModelSerializer):
    question_answer = QuestionSerializer(many=True, required=False)

    class Meta:
        model = UserAnswer
        fields = ('id', 'question_answer', 'answer')
        read_only_fields = ('id',)

    def create(self, validated_data):
        # TODO save trial number to be able to show all the trials for a user
        user = User.objects.get(id=self.context.get('user').id)
        question_answer = validated_data.pop('question_answer')
        for i in range(0, len(question_answer)):
            question_answer_dict = {
                'question': Question.objects.get(id=question_answer[i]['id']),
                'answer': validated_data.pop('answer')
            }
            user_answers = UserAnswer.objects.create(**question_answer_dict)
            user_answers.user = user
            user_answers.save()

        return user_answers
