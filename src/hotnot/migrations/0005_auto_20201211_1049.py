# Generated by Django 3.0.6 on 2020-12-11 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotnot', '0004_person_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='hot_vote',
        ),
        migrations.RemoveField(
            model_name='person',
            name='not_vote',
        ),
    ]
