# Generated by Django 2.1.5 on 2019-01-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('official_website', models.URLField(blank=True)),
                ('accepted', models.BooleanField(default=False)),
                ('descprition', models.TextField()),
                ('proof', models.TextField(help_text='Put here any information about hackathon and optional links to facebookevent or official website ')),
            ],
        ),
    ]
