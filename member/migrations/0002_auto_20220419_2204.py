# Generated by Django 3.1.4 on 2022-04-19 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_model',
            name='Percentage_in_10th',
        ),
        migrations.RemoveField(
            model_name='register_model',
            name='Percentage_in_12th',
        ),
    ]