# Generated by Django 3.0 on 2021-05-13 05:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210430_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='uploadlevel',
            field=models.CharField(default=5, max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 13, 5, 40, 12, 410708, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history',
            name='leakdetetcetedat',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 13, 5, 40, 12, 411707, tzinfo=utc)),
        ),
    ]
