# Generated by Django 4.2 on 2023-04-20 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('goal', models.IntegerField(choices=[(1, 'Weight Loss'), (2, 'Muscle Gain'), (3, 'Strength Gain'), (4, 'Endurance Gain'), (5, 'General Fitness')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('fitness_experience', models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Professional')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('type', models.IntegerField(choices=[(1, 'Strength'), (2, 'Endurance'), (3, 'General Fitness'), (4, 'Metabolic Conditioning')], default=3)),
                ('audience', models.IntegerField(choices=[(1, 'Individual'), (2, 'Group')], default=1)),
                ('fitness_goal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitgptapi.fitnessgoal')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitgptapi.user')),
            ],
        ),
        migrations.AddField(
            model_name='fitnessgoal',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitgptapi.user'),
        ),
    ]