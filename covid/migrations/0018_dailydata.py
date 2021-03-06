# Generated by Django 3.0.5 on 2020-05-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0017_delete_dailydata'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
                ('totalcase', models.IntegerField()),
                ('newcase', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('newdeath', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
