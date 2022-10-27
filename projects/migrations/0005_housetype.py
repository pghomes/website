# Generated by Django 4.1.1 on 2022-09-29 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_facilities_facility'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(blank=True, max_length=250, null=True)),
                ('House_specification', models.CharField(help_text='Enter a brief specification of the product', max_length=300)),
                ('House_floor_area', models.PositiveBigIntegerField(help_text='Enter the net floor area for the product')),
                ('units', models.PositiveIntegerField(blank=True, null=True)),
                ('house_outright_payment', models.DecimalField(decimal_places=2, default=0, help_text='Enter the outright payment price', max_digits=12)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]