# Generated by Django 3.1.2 on 2021-04-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='id',
        ),
        migrations.AlterField(
            model_name='match',
            name='unique_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
