# Generated by Django 4.2 on 2023-04-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitgptapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitnessprogram',
            name='type',
        ),
        migrations.AlterField(
            model_name='fitnessgoal',
            name='goal',
            field=models.IntegerField(choices=[(1, 'Weight Loss'), (2, 'Strength Gain'), (3, 'Endurance Gain'), (4, 'General Fitness'), (5, 'Metabolic Conditioning Gain')], default=1),
        ),
    ]