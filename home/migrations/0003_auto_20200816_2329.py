# Generated by Django 3.1 on 2020-08-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactformmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='message',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
