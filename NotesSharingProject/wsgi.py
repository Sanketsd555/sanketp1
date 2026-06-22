import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NotesSharingProject.settings')

import django
from django.conf import settings
from django.core.management import call_command

django.setup()

# Auto-run migrations if tables don't exist (handles SQLite on Render)
try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1 FROM auth_user LIMIT 1")
except Exception:
    call_command('migrate', '--noinput')

# Auto-create admin if no staff user exists
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_staff=True).exists():
    admin_user = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_pass = os.environ.get('ADMIN_PASSWORD', 'admin123')
    User.objects.create_superuser(username=admin_user, password=admin_pass, email='admin@noteshare.com')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
