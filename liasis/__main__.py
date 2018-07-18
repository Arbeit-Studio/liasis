import argparse
from __version__ import __version__

# TODO: Finish this!
def new(args):
    print(args)

parser = argparse.ArgumentParser(prog='liasis', description="Liasis Command Line Interface")
parser._optionals.title = 'options'
parser.add_argument('-v,--version', action='version', version=f'%(prog)s {__version__}')
subparsers = parser.add_subparsers(
    title='commads',
    help='Available commands')

parser_new = subparsers.add_parser('new',help='Create things, like a project or apps.')
parser_new.add_argument('what', choices=['project', 'app'], help='What do you want to create?')
parser_new.add_argument('name', help='What do you want to call it?')
parser_new.set_defaults(function=new)

args = parser.parse_args()
args.function(args)

