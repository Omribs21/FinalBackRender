# Generated by Django 3.2.16 on 2022-12-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_personalproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_details',
            name='comments',
            field=models.CharField(default='', max_length=150),
        ),
    ]