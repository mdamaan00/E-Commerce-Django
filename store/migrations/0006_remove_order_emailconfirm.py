# Generated by Django 3.1.1 on 2021-04-26 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210427_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='emailconfirm',
        ),
    ]