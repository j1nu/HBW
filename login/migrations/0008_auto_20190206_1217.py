# Generated by Django 2.1.2 on 2019-02-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_studytable_starttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studytable',
            name='StartTime',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='EndTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='StartTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='table_borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='unbrella_borrowed',
            field=models.BooleanField(default=False),
        ),
    ]