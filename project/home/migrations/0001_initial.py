# Generated by Django 3.0.2 on 2020-01-14 09:26

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
                ('name', models.CharField(max_length=10, unique=True)),
                ('homepage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_type', models.CharField(choices=[('vn', '.vn'), ('com', '.com'), ('comvn', '.com.vn'), ('net', '.net'), ('org', '.org'), ('info', '.info')], default='vn', max_length=10)),
                ('origin_price', models.CharField(default='0', max_length=20)),
                ('sale_price', models.CharField(default='0', max_length=20)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Vendor')),
            ],
        ),
    ]