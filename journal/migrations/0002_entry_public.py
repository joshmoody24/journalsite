# Generated by Django 3.2.9 on 2022-05-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
