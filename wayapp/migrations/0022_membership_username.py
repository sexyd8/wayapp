# Generated by Django 3.2.9 on 2021-12-10 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wayapp', '0021_auto_20211210_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wayapp.profile'),
        ),
    ]
