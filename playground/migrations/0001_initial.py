# Generated by Django 5.0.3 on 2024-03-07 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoption_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=25)),
                ('adoption_date', models.DateField(max_length=20)),
                ('notes', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField(max_length=2)),
                ('work', models.TextField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('species', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=25)),
                ('age', models.IntegerField(max_length=2)),
                ('picture', models.CharField(max_length=1000)),
                ('adoption_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='playground.adoption_status')),
            ],
        ),
        migrations.AddField(
            model_name='adoption_status',
            name='adopted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='playground.user'),
        ),
    ]