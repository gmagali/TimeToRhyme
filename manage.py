#!/usr/bin/env python
import os
import sys
from  TimeToRhyme  import find_rhyme
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TimeToRhyme.settings")
    find_rhyme.makeDic() # initial dic
    find_rhyme.makeDicRhyms() # initial dic
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
