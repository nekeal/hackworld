# Generated by Django 2.1.5 on 2019-01-12 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('looking_for', models.BooleanField()),
                ('members', models.ManyToManyField(related_name='teams', to='people.Participant')),
                ('teamleader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Participant')),
            ],
        ),
    ]
