# Generated by Django 5.0.7 on 2024-11-19 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0004_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sect_num', models.IntegerField()),
                ('sect_title', models.CharField(max_length=255)),
                ('about_desc', models.TextField()),
            ],
        ),
    ]