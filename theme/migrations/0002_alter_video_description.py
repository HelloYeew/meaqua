# Generated by Django 4.0.6 on 2022-07-27 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
