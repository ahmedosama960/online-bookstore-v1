# Generated by Django 3.2.3 on 2021-08-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_useraddress_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
