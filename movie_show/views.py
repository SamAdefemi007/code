from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    result = Movie.objects.all().order_by("-ratings__rating")
    paginator = Paginator(result, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movie_show/index.html', {'page_obj': page_obj})
