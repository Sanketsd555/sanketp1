import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NotesSharingProject.settings')

import django
django.setup()

from django.core.management import call_command
from django.db import connection

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1 FROM auth_user LIMIT 1")
except Exception:
    call_command('migrate', '--noinput')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
