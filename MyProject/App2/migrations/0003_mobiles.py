# Generated by Django 3.0.7 on 2020-06-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0002_auto_20200630_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
                ('cost', models.FloatField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
