# Generated by Django 3.1.4 on 2020-12-14 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0006_register_model_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.AddField(
            model_name='register_model',
            name='author',
            field=models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, to='members.author'),
            preserve_default=False,
        ),
    ]