# Generated by Django 3.2.9 on 2021-12-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayapp', '0015_alter_profile_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='fee',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fee',
            field=models.FloatField(),
        ),
    ]
