from django.urls import path, include
from .views import get_section1_questions, get_section2_questions,\
    create_business_plan_submission


urlpatterns = [
    path('section1/questions', get_section1_questions),
    path('section2/questions', get_section2_questions),
    path('submission', create_business_plan_submission),

]