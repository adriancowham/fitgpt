# Generated by Django 4.2 on 2023-04-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitgptapi', '0009_prompt'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='sequence_num',
            field=models.IntegerField(null=True),
        ),
    ]
