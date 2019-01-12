# Generated by Django 2.1.5 on 2019-01-12 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import people.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='added_by',
            field=models.ForeignKey(default=people.models.get_user, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
