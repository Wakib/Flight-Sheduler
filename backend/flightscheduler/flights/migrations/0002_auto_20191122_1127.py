# Generated by Django 2.2.7 on 2019-11-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
