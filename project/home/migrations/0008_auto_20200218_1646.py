# Generated by Django 3.0.3 on 2020-02-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200218_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='origin_price',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
