# Generated by Django 5.0.3 on 2024-03-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
