# Generated by Django 5.0.7 on 2024-11-19 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0005_sections'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sections',
            old_name='about_desc',
            new_name='sect_desc',
        ),
    ]
