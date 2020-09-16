#!D:\API_Test\venv\Scripts\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'xdot==1.1','gui_scripts','xdot'
__requires__ = 'xdot==1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('xdot==1.1', 'gui_scripts', 'xdot')()
    )
