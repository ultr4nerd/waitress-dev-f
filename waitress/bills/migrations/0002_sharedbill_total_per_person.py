# Generated by Django 2.2.3 on 2019-07-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedbill',
            name='total_per_person',
            field=models.FloatField(default=0, verbose_name='total por persona'),
        ),
    ]