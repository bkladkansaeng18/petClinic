# Generated by Django 2.1.3 on 2018-11-28 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0016_auto_20181129_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queue',
            name='id',
        ),
        migrations.AlterField(
            model_name='queue',
            name='pet_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.mypet'),
        ),
    ]
