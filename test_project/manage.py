#!/usr/bin/env python
import os
import sys

try:
    from django.core.management import execute_manager
    import imp
    try:
        imp.find_module('settings')  # Assumed to be in the same directory.
    except ImportError:
        err_msg = "Error: Can't find the file 'settings.py' in the " + \
                  "directory containing %r. It appears you've customized " + \
                  "things.\nYou'll have to run django-admin.py, passing " + \
                  "it your settings module.\n"
        sys.stderr.write(err_msg % __file__)
        sys.exit(1)
    import settings
    if __name__ == "__main__":
        execute_manager(settings)
except ImportError:
    if __name__ == "__main__":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
