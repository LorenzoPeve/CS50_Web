# Generated by Django 4.2.4 on 2023-09-03 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.URLField(default='https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/image-not-available.jpg'),
        ),
    ]