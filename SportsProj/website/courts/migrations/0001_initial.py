# Generated by Django 4.2.6 on 2023-11-16 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('courtid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('courttype', models.CharField(default=None, max_length=15, null=True)),
                ('courtdesc', models.CharField(default=None, max_length=30, null=True)),
                ('avail', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'court',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('courtid', models.ForeignKey(db_column='courtid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='courts.court')),
                ('SRN', models.ForeignKey(db_column='SRN', on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
            options={
                'db_table': 'bookings',
            },
        ),
    ]
