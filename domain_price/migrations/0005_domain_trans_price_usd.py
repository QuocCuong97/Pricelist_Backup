# Generated by Django 3.0.3 on 2020-02-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain_price', '0004_auto_20200221_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='trans_price_usd',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
