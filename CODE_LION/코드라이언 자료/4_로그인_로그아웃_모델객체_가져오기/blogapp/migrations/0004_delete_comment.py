# Generated by Django 3.1.5 on 2021-01-29 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
