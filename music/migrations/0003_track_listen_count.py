# Generated by Django 3.1.3 on 2020-11-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20201106_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='listen_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]