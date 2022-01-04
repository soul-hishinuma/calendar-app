# Generated by Django 3.2.10 on 2022-01-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]