# Generated by Django 4.2.5 on 2023-10-11 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_download_url_project_code_download_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='field',
            new_name='project_field',
        ),
        migrations.RenameField(
            model_name='projectfield',
            old_name='field',
            new_name='project_field',
        ),
    ]
