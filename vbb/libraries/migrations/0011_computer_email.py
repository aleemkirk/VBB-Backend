# Generated by Django 3.2.13 on 2022-07-21 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0010_userpreferenceslot_is_recurring'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
