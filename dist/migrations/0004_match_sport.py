# Generated by Django 4.0 on 2022-11-03 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dist', '0003_match_result_alter_match_winner_alter_team_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='sport',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='dist.sport'),
        ),
    ]
