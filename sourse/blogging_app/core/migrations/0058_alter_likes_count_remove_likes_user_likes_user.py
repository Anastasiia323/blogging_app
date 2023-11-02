# Generated by Django 4.2.4 on 2023-10-26 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0057_alter_likes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user',
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
