# Generated by Django 4.0.1 on 2022-01-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default='hi'),
            preserve_default=False,
        ),
    ]
