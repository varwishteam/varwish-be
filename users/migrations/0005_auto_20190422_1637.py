# Generated by Django 2.2 on 2019-04-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190422_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='wishlists',
            field=models.ManyToManyField(related_name='has_wishlists', to='wishlists.Wishlist'),
        ),
    ]