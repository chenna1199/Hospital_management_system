# Generated by Django 2.2.6 on 2020-01-19 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0015_auto_20200119_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testing',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Test'),
        ),
    ]
