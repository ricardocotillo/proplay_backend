# Generated by Django 5.0.2 on 2024-03-19 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0010_alter_progroupuser_role_alter_schedule_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='name',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]