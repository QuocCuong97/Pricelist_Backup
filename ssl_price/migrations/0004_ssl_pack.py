# Generated by Django 2.1.12 on 2020-03-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_price', '0003_auto_20200302_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssl',
            name='pack',
            field=models.CharField(max_length=60, null=True),
        ),
    ]