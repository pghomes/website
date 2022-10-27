# Generated by Django 4.1.1 on 2022-09-28 13:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a product feature (e.g. Swimming-pool CCTV Solar-power)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('location', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hectares', models.DecimalField(blank=True, decimal_places=2, help_text='Enter the number of hectares', max_digits=6, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('status', models.CharField(blank=True, choices=[('NS', 'Not started'), ('OG', 'Ongoing'), ('CD', 'Completed')], default='NS', help_text='Project work status', max_length=2)),
                ('purpose', models.CharField(blank=True, choices=[('RD', 'Residential'), ('CM', 'Commercial'), ('OH', 'Others')], default='RD', help_text='Project purpose', max_length=2)),
                ('facilities', models.ManyToManyField(help_text='Select a feature for this book', to='projects.facilities')),
            ],
        ),
    ]
