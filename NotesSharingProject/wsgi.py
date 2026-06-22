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

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
