# Generated by Django 2.2.10 on 2020-02-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_auto_20200223_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='term',
            options={'ordering': ['-created_at'], 'verbose_name': 'Term', 'verbose_name_plural': 'Terms'},
        ),
        migrations.AlterField(
            model_name='term',
            name='academic_year',
            field=models.PositiveIntegerField(choices=[(2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001)]),
        ),
    ]