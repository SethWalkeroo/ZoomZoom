from clint.textui import puts, indent
from getpass import getuser

with indent(4, quote=" >"):
    puts(getuser())