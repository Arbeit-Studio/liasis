import argparse

from . import scaffold
from .__version__ import __version__


# TODO: Finish this!
def new(**kwags):
    what, name, directory, _ = kwags.values()
    command = getattr(scaffold, f'new_{what}')
    command(name, directory)


def cli():
    parser = argparse.ArgumentParser(prog='Liasis', description="Liasis Command Line Interface")
    parser._optionals.title = 'options'
    parser.add_argument('-v,--version', action='version', version=f'%(prog)s {__version__}')
    subparsers = parser.add_subparsers(
        title='commads',
        help='Available commands')

    parser_new = subparsers.add_parser('new', description='####', help='Create things, like a project or apps.')
    parser_new.add_argument('what', choices=['project', 'app'], help='What do you want to create?')
    parser_new.add_argument('name', help='What do you want to call it?')
    parser_new.add_argument('-d', '--directory', help='An optional directory path. Defaults to "." (current) directory for project sub-command and to "./apps" directory for apps sub-command.')
    parser_new.set_defaults(function=new)
    args = parser.parse_args()
    
    if vars(args):
        # This validation is required to avoid an AttributeError: 'Namespace' 
        # object has no attribute 'function' exception.
        # I don't know exactly why this happens but it ignores the default
        # argument 'function' set previously when there's no other arguments.
        args.function(**vars(args))


if __name__ == '__main__':
    cli()
