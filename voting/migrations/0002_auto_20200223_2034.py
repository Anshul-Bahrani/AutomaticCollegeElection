# Generated by Django 2.2.10 on 2020-02-23 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nominee',
            options={'ordering': ['-created_at'], 'verbose_name': 'Nominee', 'verbose_name_plural': 'Nominees'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['-created_at'], 'verbose_name': 'Position', 'verbose_name_plural': 'Positions'},
        ),
    ]