# Generated by Django 5.0.7 on 2024-11-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0002_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=255)),
                ('about_desc', models.TextField()),
            ],
        ),
    ]
