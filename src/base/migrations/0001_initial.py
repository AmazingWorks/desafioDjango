from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import migrations
from django.conf import settings


def forward(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(email='admin@admin.com').exists():
        User.objects.create_superuser(email='admin@admin.com', password='adminadmin', nome='Administrador')


def reverte(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(forward, reverte),
    ]
