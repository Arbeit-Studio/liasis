from pathlib import Path

def new_project(name: str, directory: str = None) -> None:
    directory = '.' if directory is None else directory
    print('project', name, directory)


def new_app(name: str, directory: str = None) -> None:
    directory = './apps' if directory is None else directory
    print('app', name, directory)