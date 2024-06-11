# Generated by Django 3.2.13 on 2022-07-18 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraries', '0007_auto_20220707_2234'),
        ('profiles', '0014_alter_mentorprofile_assigned_library'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.library')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
