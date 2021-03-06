# Generated by Django 2.1.2 on 2018-11-07 05:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_date', models.DateField(default=datetime.date.today)),
                ('symptom', models.CharField(max_length=255)),
                ('medicine', models.CharField(max_length=255)),
                ('monation', models.CharField(max_length=255)),
                ('veterinarian', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='queue',
            fields=[
                ('pet_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.mypet')),
                ('pet_weight', models.CharField(default='', max_length=255)),
                ('pet_HeartRate', models.CharField(default='', max_length=30)),
                ('pet_restRate', models.CharField(default='', max_length=30)),
                ('pet_Dehydration', models.CharField(default='', max_length=30)),
                ('pet_want', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_date', models.DateField(default=datetime.date.today)),
                ('immunization', models.CharField(max_length=255)),
                ('vaccine', models.CharField(max_length=255)),
                ('dose', models.CharField(max_length=255)),
                ('next_due', models.CharField(max_length=255)),
                ('veterinarian', models.CharField(max_length=255)),
                ('pet_name', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='user.mypet')),
            ],
        ),
        migrations.AddField(
            model_name='medical',
            name='pet_name',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='user.mypet'),
        ),
    ]
