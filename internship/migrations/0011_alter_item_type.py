# Generated by Django 3.2.21 on 2023-12-19 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0010_auto_20231220_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='internships', to='internship.type'),
        ),
    ]
