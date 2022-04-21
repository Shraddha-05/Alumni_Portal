# Generated by Django 3.1.4 on 2022-04-19 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('Home_Town', models.CharField(max_length=120)),
                ('Join_Year', models.CharField(max_length=120)),
                ('Passout_Year', models.CharField(max_length=120)),
                ('Ph_No', models.CharField(max_length=120)),
                ('CGPA', models.CharField(max_length=120)),
                ('Percentage_in_10th', models.CharField(max_length=120)),
                ('Percentage_in_12th', models.CharField(max_length=120)),
                ('Branch', models.CharField(max_length=120)),
                ('Semester', models.IntegerField()),
                ('Batch', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=254)),
                ('company_Name', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('designation', models.CharField(max_length=120)),
                ('work_area', models.CharField(max_length=120)),
                ('Specification', models.CharField(max_length=120)),
                ('Experience', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]