# Generated by Django 2.0 on 2019-08-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stats_name', models.CharField(max_length=30, null=True)),
                ('stats_image', models.FileField(null=True, upload_to='')),
                ('stats_num', models.IntegerField(null=True)),
            ],
        ),
    ]
