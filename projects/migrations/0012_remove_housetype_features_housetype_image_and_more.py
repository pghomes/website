# Generated by Django 4.1.1 on 2022-10-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_project_hectares'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housetype',
            name='features',
        ),
        migrations.AddField(
            model_name='housetype',
            name='image',
            field=models.ImageField(default=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='housetype',
            name='status',
            field=models.CharField(blank=True, choices=[('For Rent', 'For Rent'), ('For Sales', 'For Sale')], default='For Sale', help_text='House Type status', max_length=50),
        ),
    ]
