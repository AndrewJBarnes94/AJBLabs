# Generated by Django 4.2.5 on 2023-11-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biz', '0002_davinci002_query_log_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectManagerAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_prompt', models.CharField()),
                ('prompt', models.CharField()),
                ('post_prompt', models.CharField()),
                ('response', models.CharField(null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]