# Generated by Django 3.2.3 on 2021-05-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
