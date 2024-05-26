# urls.py is written to call the view created in views.py
# This maps it to a URL using URLconf

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]