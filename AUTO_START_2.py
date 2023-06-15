import subprocess

def open_terminal():
    project_path = '/Volumes/Private/vetrof/Dropbox/GitHub/parsing_bus_ind'
    venv_path = 'venv/'
    script = f'''
        tell application "Terminal"
            do script "cd {project_path} && source {venv_path}/bin/activate && python all0none.py"
        end tell
    '''
    subprocess.call(['osascript', '-e', script])

open_terminal()
