# Generated by Django 5.1.6 on 2025-02-18 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autho',
            new_name='author',
        ),
    ]
