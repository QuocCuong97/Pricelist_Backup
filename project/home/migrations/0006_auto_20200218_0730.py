# Generated by Django 3.0.2 on 2020-02-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200217_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='vps',
            name='core',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='vps',
            name='cpu',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
