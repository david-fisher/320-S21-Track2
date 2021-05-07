#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD:segfault/manage.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'segfault.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shibdjango.settings')
>>>>>>> a769e79061984da2b18b10b544a5b1a1a3200162:shibdjango/ethisim.cs.umass.edu/manage.py
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
