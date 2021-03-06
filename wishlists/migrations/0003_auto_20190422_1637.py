# Generated by Django 2.2 on 2019-04-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0002_wishlist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='wishlist',
            name='items',
            field=models.ManyToManyField(to='wishlists.Item'),
        ),
    ]
