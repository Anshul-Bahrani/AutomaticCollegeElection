# Generated by Django 2.2.10 on 2020-02-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffCtCcAllotment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('term', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]