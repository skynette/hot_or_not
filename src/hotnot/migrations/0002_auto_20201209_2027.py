# Generated by Django 3.0.6 on 2020-12-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotnot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, height_field=300, max_length=50, null=True, upload_to='', width_field=300),
        ),
    ]
