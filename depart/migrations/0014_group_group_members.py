# Generated by Django 2.0.6 on 2019-11-26 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('depart', '0013_auto_20191005_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_members',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='group', to=settings.AUTH_USER_MODEL),
        ),
    ]