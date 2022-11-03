from django.contrib import admin
from .models import Sport, Team, Match, Cluster, Score ,    Edit
# Register your models here.
admin.site.register(Edit)
admin.site.register(Sport)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Cluster)
admin.site.register(Score)