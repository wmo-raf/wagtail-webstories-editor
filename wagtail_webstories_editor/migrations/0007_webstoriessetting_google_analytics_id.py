# Generated by Django 4.2.6 on 2023-10-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_webstories_editor', '0006_webstoriespublisherlogo_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='webstoriessetting',
            name='google_analytics_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Google Analytics Measurement ID'),
        ),
    ]
