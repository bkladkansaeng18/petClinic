# Generated by Django 2.1.3 on 2018-11-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_appointment_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical',
            name='age',
            field=models.CharField(default=5, max_length=30),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='age',
            field=models.CharField(default=5, max_length=30),
        ),
    ]
