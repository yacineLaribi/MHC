# Generated by Django 3.2.21 on 2023-12-21 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newrequestmodel',
            name='requested_to',
        ),
    ]
