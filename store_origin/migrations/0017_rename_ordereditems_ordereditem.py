# Generated by Django 4.1.2 on 2022-12-12 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_origin', '0016_alter_item_options_ordereditems_alter_order_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderedItems',
            new_name='OrderedItem',
        ),
    ]
