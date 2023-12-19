# Generated by Django 3.2.21 on 2023-12-19 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0015_rename_typee_item_type_is'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='type_is',
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]