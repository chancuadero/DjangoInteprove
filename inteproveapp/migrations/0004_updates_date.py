# Generated by Django 4.1.6 on 2023-05-27 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inteproveapp', '0003_updates_alter_investor_aa'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
