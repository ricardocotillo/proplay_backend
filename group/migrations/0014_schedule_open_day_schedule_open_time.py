# Generated by Django 5.0.2 on 2024-04-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0013_remove_session_num_players_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='open_day',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='open_time',
            field=models.TimeField(default='9:00'),
            preserve_default=False,
        ),
    ]
