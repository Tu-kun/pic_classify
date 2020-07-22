#!E:\tu\pycharmWorkplace\lac\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'LAC==2.0.4','console_scripts','lac'
__requires__ = 'LAC==2.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('LAC==2.0.4', 'console_scripts', 'lac')()
    )
