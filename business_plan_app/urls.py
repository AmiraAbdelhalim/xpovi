from django.urls import path, include
from .views import get_section1_questions, get_section2_questions,\
    create_business_plan_submission, get_new_trial_number, get_current_trial_submitted_answers


urlpatterns = [
    path('section1/questions', get_section1_questions),
    path('section2/questions', get_section2_questions),
    path('trial', get_new_trial_number),
    path('submission/<int:trial_num>', create_business_plan_submission),
    path('answers/<int:trial_number>', get_current_trial_submitted_answers),

]