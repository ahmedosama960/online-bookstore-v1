# Generated by Django 3.2.3 on 2021-05-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210526_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='total_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
