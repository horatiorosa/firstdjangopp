#tuns commands for our project
#do not edit this file, best to leave as is
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myfirstdjangopp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
