from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from business_plan_app.serializers import QuestionSerializer, AnswerSerializer
from .models import *


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
def create_business_plan_submission(request):
    """
    :param request:
    :return:
    """
    answer_serializer = AnswerSerializer(data=request.data, context={'user': request.user}, many=True)
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

# TODO endpoint to get business plan
