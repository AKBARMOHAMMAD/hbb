# Generated by Django 2.1.4 on 2018-12-14 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akbarhotel', '0006_display_room_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='display',
            name='CUSTOMER_ID',
        ),
    ]
