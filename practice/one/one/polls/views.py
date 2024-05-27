from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # use render if i have a template
    # return render("Hi")
    return HttpResponse("word")