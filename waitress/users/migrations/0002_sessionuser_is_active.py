# Generated by Django 2.2.3 on 2019-07-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionuser',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='activo'),
        ),
    ]