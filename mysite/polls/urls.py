# urls.py is written to call the view created in views.py
# This maps it to a URL using URLconf

from django.urls import path
from . import views

# Added to namespace URL names to differentiate {% url %} template tags
app_name = "polls"

# This is where you name and assign urls
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/result/", views.result, name="result"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")
]

# Using angle brackets “captures” part of the URL and sends it as a 
# keyword argument to the view function. The question_id part of the 
# string defines the name that will be used to identify the matched 
# pattern, and the int part is a converter that determines what patterns
# should match this part of the URL path. The colon (:) separates the 
# converter and pattern name.