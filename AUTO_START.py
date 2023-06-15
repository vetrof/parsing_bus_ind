virtualenv_path = '/Volumes/Private/vetrof/Dropbox/GitHub/parsing_bus_ind/venv/bin/activate'

import subprocess

def open_terminal():
    script = 'tell app "Terminal" to do script "cd /Volumes/Private/vetrof/Dropbox/GitHub/parsing_bus_ind && source venv/bin/activate && python all0none.py"'
    subprocess.call(['osascript', '-e', script])
open_terminal()
