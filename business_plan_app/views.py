from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from business_plan_app.serializers import QuestionSerializer, AnswerSerializer
from .models import *
from django.db.models import Max


@permission_classes([IsAuthenticated])
@api_view(['GET', ])
def get_section1_questions(request):
    """
    return section 1 questions and their possible answers
    :return:
    """
    try:
        section1_questions = Question.objects.filter(section="s1")
        if section1_questions:
            questions_serializer = QuestionSerializer(section1_questions, many=True)

            data = {
                'response_id': "0",
                'data': questions_serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        data = {
            'response_id': "1",
            'data': "There is no questions in section1"
        }
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        print(f'an exception occurred --> {e}')
        data = {
            'response_id': "-1",
            'error': f'{e} occurred please contact admin!'
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET', ])
def get_section2_questions(request):
    """
    return section 2 questions and their possible answers
    :return:
    """
    try:
        section2_questions = Question.objects.filter(section="s2")
        if section2_questions:
            questions_serializer = QuestionSerializer(section2_questions, many=True)
            data = {
                'response_id': "0",
                'data': questions_serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        data = {
            'response_id': "1",
            'data': "There is no questions in section1"
        }
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        print(f'an exception occurred --> {e}')
        data = {
            'response_id': "-1",
            'error': f'{e} occurred please contact admin!'
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['POST', ])
def create_business_plan_submission(request, trial_num):
    """
    :param trial_num:
    :param request:
    :return:
    """
    try:
        trial_exist = UserTrial.objects.get(trial_num=trial_num, user=request.user)
    except Exception as e:
        print('exception=> ', e)
        trial_exist = []
    if trial_exist:
        data = {"response_id": "-1", "error": "trial already exist!"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    answer_serializer = AnswerSerializer(data=request.data, context={'user': request.user, 'trial_num': trial_num},
                                         many=True)

    if answer_serializer.is_valid():
        try:
            answer_serializer.save()
        except Exception as e:
            print(e, '--> ', answer_serializer.errors)
            data = {"response_id": "-1", "error": "plan not created"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        data = {"response_id": "0", "data": answer_serializer.data}
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data = {"response_id": "-1", "error": answer_serializer.errors}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET', ])
def get_new_trial_number(request):
    """
    get the number of the new trial if uer didn't submit a questionnaire before
    or what should be his/her new trial number
    :param request:
    :return:
    """
    trial = UserTrial.objects.filter(user=request.user)
    last_trial = 0
    if trial.first():
        last_trial = trial.aggregate(Max('trial_num')).get('trial_num__max')
    data = {
        'response_id': 0,
        'trial_num': last_trial + 1
    }
    return Response(data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['GET', ])
# FIXME: find a way to display question instead of question number
def get_current_trial_submitted_answers(request, trial_number):
    """

    :param request:
    :param trial_number:
    :return:
    """
    trial = UserTrial.objects.get(trial_num=trial_number, user=request.user)
    answers = UserAnswer.objects.filter(trial=trial, user=request.user)
    if not answers:
        data = {
            'response_id': "-1",
            'error': 'No Answers'
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    answers_serializer = AnswerSerializer(answers, many=True)
    data = {
        'response_id': "0",
        'data': answers_serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)
# TODO update submission endpoint
