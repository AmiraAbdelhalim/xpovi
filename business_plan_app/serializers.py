from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    question = serializers.CharField(required=False)

    class Meta:
        model = Question
        fields = ('id', 'question', 'type')
        read_only_fields = ('id',)


class TrialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = UserTrial
        fields = '__all__'


class AnswerListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        answer_mapping = {answer.id: answer for answer in instance}

        data_mapping = {item['id']: item for item in validated_data}
        ret = []
        for answer_id, data in data_mapping.items():
            answer = answer_mapping.get(answer_id)
            if answer:
                ret.append(self.child.update(answer, data))
        return ret


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    question_answer = QuestionSerializer(many=True, required=False)
    trial_number = TrialSerializer(many=True, required=False)

    class Meta:
        list_serializer_class = AnswerListSerializer
        model = UserAnswer
        fields = '__all__'
        read_only_fields = ('id', 'question',)

    def create(self, validated_data):
        user = User.objects.get(id=self.context.get('user').id)
        trial = UserTrial.objects.filter(trial_num=self.context.get('trial_num'))
        if not trial:
            new_trial = UserTrial.objects.create(trial_num=self.context.get('trial_num'), user=user)
        else:
            new_trial = trial.first()

        question_answer = validated_data.pop('question_answer')
        for i in range(0, len(question_answer)):
            question_answer_dict = {
                'question': Question.objects.get(id=question_answer[i]['id']),
                'choices_answer': validated_data.pop('choices_answer'),
                'int_answer': validated_data.pop('int_answer'),
                'trial': new_trial,
                'user': user
            }
            print('json ', question_answer_dict)
            user_answers = UserAnswer.objects.create(**question_answer_dict)
        return user_answers
