# Generated by Django 5.1.5 on 2025-01-30 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='name',
            new_name='note',
        ),
    ]
