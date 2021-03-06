# Generated by Django 2.2.10 on 2020-02-23 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_auto_20200223_2128'),
        ('voting', '0002_auto_20200223_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='term',
        ),
        migrations.AddField(
            model_name='election',
            name='term_id',
            field=models.ForeignKey(default=1415, on_delete=django.db.models.deletion.DO_NOTHING, to='academics.Term'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='election',
            name='duration',
            field=models.DurationField(),
        ),
    ]
