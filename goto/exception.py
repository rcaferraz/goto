# coding: utf-8
import sys

def warning_and_exit(error):
    """
    Prints a string `error` into stderr and exits with status code equals to 1.
    """
    sys.stderr.write(error + '\n')
    sys.exit(1)
