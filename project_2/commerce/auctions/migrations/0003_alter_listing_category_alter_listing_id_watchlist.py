# Generated by Django 4.2.4 on 2023-09-05 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_listing_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Home & Furniture', 'Home & Furniture'), ('Health & Beauty', 'Health & Beauty'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Toys & Games', 'Toys & Games'), ('Books & Media', 'Books & Media'), ('Automotive', 'Automotive'), ('Collectibles & Art', 'Collectibles & Art')], max_length=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]