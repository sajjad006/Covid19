# Generated by Django 3.0.5 on 2020-04-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0009_auto_20200427_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrydata',
            name='death_pop',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='countrydata',
            name='test_pop',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='countrydata',
            name='total_pop',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
