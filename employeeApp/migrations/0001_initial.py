# Generated by Django 3.2.4 on 2021-06-24 16:15

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
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.CharField(max_length=20)),
                ('empname', models.CharField(max_length=50)),
                ('empemail', models.EmailField(max_length=254)),
                ('empactive', models.CharField(choices=[('1', 'user Active'), ('0', 'user offline')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]