# Generated by Django 2.1.5 on 2019-01-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_hackathon_max_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='place',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='place_url',
            field=models.URLField(blank=True),
        ),
    ]
