# Generated by Django 4.1.2 on 2022-12-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_origin', '0007_item_item_it_alter_item_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='vendor_code',
            field=models.CharField(default='AF3FT15FXPEROIBUDEMF', max_length=20, unique=True, verbose_name='Артикул'),
        ),
    ]