# Generated by Django 3.2.7 on 2021-10-04 21:13
# pylint: skip-file
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0005_alter_scheduledemail_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledemail',
            name='cc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
