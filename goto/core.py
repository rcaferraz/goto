# coding: utf-8
import sys
from goto import get_version
from exception import warning_and_exit


def print_help(error=False, msg=None):
    """"""
    if error:
        f = sys.stderr
        status = -1
    else:
        f = sys.stdout
        status = 0

    if msg:
        f.write(msg + '\n')
    f.write("TODO WRITE HELP!" + '\n')
    sys.exit(status)


def print_version():
    """"""
    print "goto version %s." % get_version()
    sys.exit(0)
