# Generated by Django 4.1.2 on 2022-11-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_origin', '0005_alter_item_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='vendor_code',
            field=models.CharField(default='M4GCP90WCSLHA7N087K9', max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Артикул'),
        ),
    ]
