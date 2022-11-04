from django.shortcuts import render ,get_object_or_404
from .models import *
from django.db.models import Sum
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
    if sport_id:
        matchs = Match.objects.filter(sport=sport_id.id)
    else:
        matchs = []
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
    data={}
    for obj in cluster:
        score = Score.objects.filter(cluster=obj.id).order_by('-Score')
        total_score=score.aggregate(Sum('Score'))
        data[obj.name]={'score':score,'total':total_score} 
    score = Score.objects.all()
    sports = Sport.objects.all()
    print(data)
    context = {
       'data':data,
        'sports': sports,
        
    }
    return render(request, 'cluster.html', context)