# Generated by Django 3.0.3 on 2020-02-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain_price', '0002_auto_20200220_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='renew_price',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='domain',
            name='trans_price',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
