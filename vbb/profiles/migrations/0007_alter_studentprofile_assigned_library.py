# Generated by Django 4.0.3 on 2022-05-13 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0002_library_library_code'),
        ('profiles', '0006_alter_mentorprofile_assigned_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='assigned_library',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libraries.library'),
        ),
    ]
