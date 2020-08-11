# Generated by Django 3.0.7 on 2020-06-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0003_mobiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
        ),
    ]