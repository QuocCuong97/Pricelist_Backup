# Generated by Django 3.0.3 on 2020-02-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('homepage', models.CharField(max_length=30, unique=True)),
                ('logo', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_type', models.CharField(choices=[('vn', '.vn'), ('com', '.com'), ('comvn', '.com.vn'), ('net', '.net'), ('org', '.org'), ('info', '.info')], default='vn', max_length=10)),
                ('reg_origin', models.DecimalField(decimal_places=3, max_digits=8)),
                ('reg_promotion', models.DecimalField(decimal_places=3, max_digits=8)),
                ('renew_price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('trans_price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('usd', models.CharField(blank=True, max_length=6)),
                ('note', models.TextField(blank=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain_price.Vendor')),
            ],
        ),
    ]
