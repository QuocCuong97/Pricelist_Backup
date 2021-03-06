# Generated by Django 2.1.12 on 2020-03-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_price', '0002_auto_20200302_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssl',
            name='validation_type',
            field=models.CharField(choices=[('DV', 'Domain Validation (DV)'), ('EV', 'Extended Validation (EV)'), ('OV', 'Organization Validation (OV)')], default='DV', max_length=30),
        ),
    ]
