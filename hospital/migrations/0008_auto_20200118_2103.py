# Generated by Django 2.2.6 on 2020-01-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_discharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='discharge',
            name='date1',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='discharge',
            name='time1',
            field=models.TimeField(null=True),
        ),
    ]
