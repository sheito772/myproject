from django.db import migrations
from django.contrib.auth.models import User
import os

def create_superuser(apps, schema_editor):
    username = os.environ.get('SUPERUSER_NAME')
    password = os.environ.get('SUPERUSER_PASSWORD')
    email = os.environ.get('SUPERUSER_EMAIL')

    if username and password:
        User.objects.create_superuser(username=username, password=password, email=email)

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
