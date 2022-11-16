# Generated by Django 3.2.13 on 2022-11-16 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0005_auto_20221116_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercard',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_card', to=settings.AUTH_USER_MODEL),
        ),
    ]
