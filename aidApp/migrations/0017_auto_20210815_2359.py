# Generated by Django 3.2.4 on 2021-08-16 03:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0016_auto_20210805_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='app_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 16, 3, 59, 42, 477473, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='D_O_B',
            field=models.DateField(default=datetime.datetime(2021, 8, 16, 3, 59, 42, 470474, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='telephone',
            field=phone_field.models.PhoneField(blank=True, help_text='Patient phone number', max_length=31),
        ),
    ]