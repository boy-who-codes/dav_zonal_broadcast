# Generated by Django 4.0 on 2022-11-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dist', '0006_remove_cluster_teams_cluster_total_score_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
    ]
