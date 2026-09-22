import os
import logging
from pathlib import Path


project_name = 'textSummarizer'

list_of_files = [
    'logging.py',
    'exception.py',
    'requirements.txt',
    'setup.py',
    'app.py',
    'main.py',
    'config/config.yaml',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/contants/__init__.py',
    f'src/{project_name}/config/__init__.py',

    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/configuration.py',

    'notebook/trails.ipynb'
]


for filepath in list_of_files:
    filepath = Path(filepath)
    fileDir, filename = os.path.split(filepath)

    # create directory
    if fileDir != '':
        os.makedirs(fileDir, exist_ok=True)

    # create files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass