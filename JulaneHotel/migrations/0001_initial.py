# Generated by Django 4.0.3 on 2022-03-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomtype', models.CharField(max_length=20)),
                ('timeslot', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]