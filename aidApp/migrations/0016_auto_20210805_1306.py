# Generated by Django 3.2.4 on 2021-08-05 17:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0015_auto_20210805_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='app_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 17, 6, 39, 922864, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='D_O_B',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 17, 6, 39, 920866, tzinfo=utc)),
        ),
    ]
