# Generated by Django 4.1.1 on 2022-09-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_installmental_payment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, help_text='Enter the description', max_length=500, null=True)),
                ('minimum_amount', models.DecimalField(decimal_places=2, default=0, help_text='Enter minimum investment amount', max_digits=12)),
                ('maximum_amount', models.DecimalField(decimal_places=2, default=0, help_text='Enter maximum investment amount', max_digits=12)),
                ('roi', models.PositiveIntegerField(help_text='Enter the ROI of investment', max_length=3)),
                ('duration', models.CharField(blank=True, choices=[('AN', 'Anually'), ('MN', 'Monthly')], default='BD', help_text='Investment duration status', max_length=2)),
            ],
        ),
    ]
