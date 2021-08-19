# Generated by Django 3.2.4 on 2021-08-15 20:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0026_auto_20210815_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='health_practitioner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='app_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 15, 20, 51, 33, 61324, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='D_O_B',
            field=models.DateField(default=datetime.datetime(2021, 8, 15, 20, 51, 33, 49311, tzinfo=utc)),
        ),
    ]