# Generated by Django 4.1.2 on 2022-11-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_origin', '0004_alter_item_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='vendor_code',
            field=models.CharField(default='HIUMBRY906GBBNXO75ZZ', max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Артикул'),
        ),
    ]