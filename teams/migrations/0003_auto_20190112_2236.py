# Generated by Django 2.1.5 on 2019-01-12 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20190112_2212'),
        ('teams', '0002_team_hackathon'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='candidates',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Participant'),
        ),
        migrations.AlterField(
            model_name='team',
            name='teamleader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_teams', to='people.Participant'),
        ),
    ]
