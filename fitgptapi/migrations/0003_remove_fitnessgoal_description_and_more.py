# Generated by Django 4.2 on 2023-04-20 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitgptapi', '0002_remove_fitnessprogram_type_alter_fitnessgoal_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitnessgoal',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fitnessprogram',
            name='description',
        ),
    ]