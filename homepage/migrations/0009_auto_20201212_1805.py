# Generated by Django 3.1.4 on 2020-12-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20201212_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='adm_staff',
            name='profile_pic',
            field=models.ImageField(default='default', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumni',
            name='PROFILE_PIC',
            field=models.ImageField(default='default', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='t_p_staff',
            name='Profile_pic',
            field=models.ImageField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]