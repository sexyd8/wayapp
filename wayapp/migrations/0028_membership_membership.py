# Generated by Django 3.2.9 on 2021-12-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayapp', '0027_auto_20211215_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='membership',
            field=models.CharField(default='new', max_length=50),
        ),
    ]
