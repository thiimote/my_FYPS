# Generated by Django 2.0.6 on 2019-11-26 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0022_auto_20191126_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to=settings.AUTH_USER_MODEL),
        ),
    ]