# Generated by Django 4.2.1 on 2023-11-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='message',
            field=models.TextField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='friend',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
    ]