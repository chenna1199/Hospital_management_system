# Generated by Django 2.2.6 on 2020-01-18 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_auto_20200118_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(null=True)),
                ('delivery_date', models.DateField(null=True)),
                ('payment', models.IntegerField(max_length=30, null=True)),
                ('test', models.CharField(max_length=30, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Patient')),
            ],
        ),
    ]
