# Generated by Django 3.2.3 on 2021-05-26 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_userorder_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
