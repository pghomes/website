# Generated by Django 4.1.1 on 2022-10-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='Empty string', max_length=250, null=True),
        ),
    ]