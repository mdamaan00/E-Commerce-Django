# Generated by Django 3.1.1 on 2021-05-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210517_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='grandtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
