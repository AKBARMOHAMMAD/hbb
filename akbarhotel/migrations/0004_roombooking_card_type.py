# Generated by Django 2.1.4 on 2018-12-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akbarhotel', '0003_auto_20181214_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='roombooking',
            name='card_type',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
