# Generated by Django 2.1 on 2019-09-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190921_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(default='default.jpg', upload_to='product_pics'),
        ),
    ]
