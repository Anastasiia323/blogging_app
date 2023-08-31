# Generated by Django 4.2.4 on 2023-08-12 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_countries_created_at_alter_notifications_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countries',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='notifications',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='twits',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]