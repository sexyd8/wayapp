# Generated by Django 3.2.9 on 2021-12-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayapp', '0029_alter_membership_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='diamond',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='gold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='wood',
            field=models.BooleanField(default=False),
        ),
    ]
