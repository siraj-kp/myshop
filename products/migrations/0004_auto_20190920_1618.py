# Generated by Django 2.1 on 2019-09-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_delete_genitemslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
    ]