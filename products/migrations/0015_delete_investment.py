# Generated by Django 4.1.1 on 2022-10-21 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_rename_title_document_product_title_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Investment',
        ),
    ]
