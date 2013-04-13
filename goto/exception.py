# coding: utf-8
import sys

def warning_and_exit(error):
    """Prints `error` into stderr and exits with status code equals to 1."""
    sys.stderr.write(error + '\n')
    sys.exit(1)
