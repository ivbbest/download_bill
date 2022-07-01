# Generated by Django 4.0.5 on 2022-07-01 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='download.client')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('sum', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateTimeField()),
                ('service', models.TextField()),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='download.client')),
                ('client_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='download.organization')),
            ],
        ),
    ]