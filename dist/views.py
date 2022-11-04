from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.


def home(request):
    sports = Sport.objects.all()
    edit = Edit.objects.all()
    context = {
        'sports': sports,
        'edit': edit
    }

    return render(request, 'base.html', context)


def match(request, name):
    sport_id = Sport.objects.filter(name=name).first()
    matchs = Match.objects.filter(sport=sport_id.id)
    sports = Sport.objects.all()
    context = {
        'match': matchs,
        'sports': sports,
        # 'teams': team,
        # 'sport': sport

    }
    return render(request, 'match.html', context)


def cluster(request):
    cluster = Cluster.objects.all()
    score = Score.objects.all()
    sports = Sport.objects.all()
    context = {
        'cluster': cluster,
        'sports': sports,
        'score': score
    }
    return render(request, 'cluster.html', context)
