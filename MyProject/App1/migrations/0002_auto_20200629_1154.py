# Generated by Django 3.0.7 on 2020-06-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
