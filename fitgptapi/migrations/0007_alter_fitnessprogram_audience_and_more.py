# Generated by Django 4.2 on 2023-04-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitgptapi', '0006_alter_fitnessprogram_audience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessprogram',
            name='audience',
            field=models.CharField(blank=True, choices=[('INDIVIDUAL', 'Individual'), ('AFFILIATE', 'Affiliate'), ('GLOBAL', 'Global')], default='INDIVIDUAL', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fitnessprogram',
            name='experience',
            field=models.CharField(blank=True, choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced'), ('PROFESSIONAL', 'Professional')], default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fitnessprogram',
            name='goal',
            field=models.CharField(blank=True, choices=[('ENDURANCE', 'Endurance'), ('METABOLIC_CONDITIONING', 'Metabolic Conditioning')], default=None, max_length=255, null=True),
        ),
    ]