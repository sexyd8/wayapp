# Generated by Django 3.2.9 on 2021-12-10 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wayapp', '0025_alter_membership_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='max',
        ),
        migrations.RemoveField(
            model_name='product',
            name='min',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Downgrade',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Upgrade',
        ),
    ]
