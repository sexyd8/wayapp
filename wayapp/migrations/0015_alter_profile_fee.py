# Generated by Django 3.2.9 on 2021-12-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayapp', '0014_alter_profile_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fee',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]