# Generated by Django 3.0.8 on 2020-07-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0004_auto_20200723_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]