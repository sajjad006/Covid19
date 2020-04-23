# Generated by Django 3.0.5 on 2020-04-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_data_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
    ]
