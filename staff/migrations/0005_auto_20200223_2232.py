# Generated by Django 2.2.10 on 2020-02-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20200223_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffctccallotment',
            name='division',
            field=models.CharField(max_length=5),
        ),
    ]
