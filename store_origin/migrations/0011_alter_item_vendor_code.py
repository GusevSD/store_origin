# Generated by Django 4.1.2 on 2022-12-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_origin', '0010_alter_item_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='vendor_code',
            field=models.CharField(default='AJQO8WRXQQ6JKWAWOR56', max_length=20, unique=True, verbose_name='Артикул'),
        ),
    ]
