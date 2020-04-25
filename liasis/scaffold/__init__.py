from typing import *
from pathlib import Path
from shutil import copytree


LIASIS_ROOT = Path(__file__).parent

PROJECT_SKELETON = Path(str(LIASIS_ROOT) + '/project_skeleton')
APP_SKELETON = Path(str(LIASIS_ROOT) + '/app_skeleton')


def new_project(name: Text, directory: Text) -> None:
    path = Path('.' if directory is None else directory)
    destination = str(path.absolute()) + '/' + name
    if path.exists():
        copytree(str(PROJECT_SKELETON.absolute()), destination)
        

def new_app(name: Text, directory: Text) -> None:
    path = Path('./apps' if directory is None else directory)
    destination = str(path.absolute()) + '/' + name
    if path.exists():
        copytree(str(APP_SKELETON.absolute()), destination)