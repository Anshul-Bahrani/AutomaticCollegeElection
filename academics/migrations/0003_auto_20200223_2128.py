# Generated by Django 2.2.10 on 2020-02-23 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_auto_20200223_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='term',
            old_name='deptartment',
            new_name='department_id',
        ),
    ]