# Generated by Django 2.1.5 on 2019-01-12 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import people.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0005_auto_20190112_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.OneToOneField(default=people.models.get_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
