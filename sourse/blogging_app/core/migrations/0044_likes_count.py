# Generated by Django 4.2.4 on 2023-10-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]