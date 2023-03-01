import subprocess
import shutil
import os

if os.path.isdir('./dist'):
    shutil.rmtree('./dist')

if not os.path.isdir('./release'):
    os.mkdir('./release')

subprocess.run('pip freeze > requirements.txt', shell=True)
subprocess.run('pyinstaller --noconfirm --onefile --noconsole --icon '
               '"D:/Github/nonogram-generator/src/nonogram_generator-logo.ico"  '
               '"D:/Github/nonogram-generator/nonogram_generator.py"', shell=True)
shutil.copytree('./src', './dist/src')
shutil.make_archive('./release/nonogram_generator', 'zip', './dist')
print('done')
