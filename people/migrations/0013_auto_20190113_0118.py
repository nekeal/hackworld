# Generated by Django 2.1.5 on 2019-01-13 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_participant_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='github_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='linkedin_url',
            field=models.URLField(blank=True),
        ),
    ]