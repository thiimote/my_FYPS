# Generated by Django 2.0.6 on 2019-09-11 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('hod_name', models.CharField(max_length=80)),
                ('hod_phone_number', models.CharField(max_length=13)),
                ('hod_email', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
                ('group_email', models.CharField(max_length=250)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='depart.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.IntegerField(unique=True)),
                ('member_phone_number', models.IntegerField(max_length=10)),
                ('member_email', models.CharField(max_length=250)),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='depart.Department')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='depart.Group')),
                ('member_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_content', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_percentage', models.IntegerField()),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='depart.Files')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=500)),
                ('project_description', models.CharField(max_length=200)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='depart.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_name', models.CharField(max_length=100)),
                ('supervisor_email', models.CharField(max_length=250)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervisors', to='depart.Department')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='supervisor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='depart.Supervisor'),
        ),
    ]
