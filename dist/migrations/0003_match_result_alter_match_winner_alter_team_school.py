# Generated by Django 4.0 on 2022-11-03 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dist', '0002_team_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='result',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='dist.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='school',
            field=models.CharField(default='', max_length=100),
        ),
    ]
