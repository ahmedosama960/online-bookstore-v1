# Generated by Django 3.2.3 on 2021-06-04 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_remove_userorder_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
