# Generated by Django 2.2 on 2019-04-30 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190423_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='wishlists',
        ),
    ]
