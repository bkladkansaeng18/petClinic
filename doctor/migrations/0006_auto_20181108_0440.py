# Generated by Django 2.1.2 on 2018-11-07 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_auto_20181107_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='queue',
            name='veterinarian',
            field=models.CharField(default='', max_length=255),
        ),
    ]
