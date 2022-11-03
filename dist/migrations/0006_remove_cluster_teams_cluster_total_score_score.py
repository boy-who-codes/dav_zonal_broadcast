# Generated by Django 4.0 on 2022-11-03 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dist', '0005_alter_match_sport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster',
            name='teams',
        ),
        migrations.AddField(
            model_name='cluster',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.IntegerField()),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dist.cluster')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dist.team')),
            ],
        ),
    ]
