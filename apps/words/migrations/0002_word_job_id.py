# Generated by Django 4.2.11 on 2024-03-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='job_id',
            field=models.UUIDField(editable=False, null=True, unique=True),
        ),
    ]
