# Generated by Django 2.1.2 on 2019-02-04 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unbrella',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('borrowed', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='Lan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='battery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='month_a4',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='today_a4',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='umbrella',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Unbrella'),
        ),
    ]