# Generated by Django 4.0.5 on 2022-07-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0006_alter_bill_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='service_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
