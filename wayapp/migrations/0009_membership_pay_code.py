# Generated by Django 3.2.9 on 2021-12-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayapp', '0008_membership_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='pay_code',
            field=models.CharField(default='3fttt', max_length=36),
        ),
    ]