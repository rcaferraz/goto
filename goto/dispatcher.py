# coding: utf-8
import sys
import argparse
import core
import goto
import label
from exception import warning_and_exit


def check_help_or_version():
    """"""
    if any([arg in ['-h', '--help'] for arg in sys.argv]):
        core.print_help()

    if any([arg in ['-v', '--version'] for arg in sys.argv]):
        core.print_version()


def run_goto_parser():
    """Runs the goto parser. If it is successful, returns the args."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("label", nargs='?')

    args, argv = parser.parse_known_args()

    if argv:
        return False, None
    else:
        return True, args


def run_extended_parser():
    """
    Runs the extended parser, which looks for arguments to run with the `label`
    subcommand.
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("subcommand", choices=["label"])
    parser.add_argument("action", choices=["add", "update", "rm"],
                                                                default="add")
    parser.add_argument('key', nargs='?')
    parser.add_argument('value', nargs='?')

    args, argv = parser.parse_known_args()

    if argv:
        return False, None
    else:
        return True, args


def dispatch_goto(args):
    """Prepares the arguments to `goto`."""
    label = args.label or None
    goto.dispatch(label)


def dispatch_extended(args):
    """Prepares the arguments to `label`."""
    key = args.key or None
    value = args.value or None

    if args.subcommand == "label":
        label.dispatch(args.action, key, value)


def main():
    """Entrypoint for the `goto` utility."""
    if check_help_or_version():
        help_or_version()
        return

    ok, args = run_goto_parser()
    if ok:
        dispatch_goto(args)
        return

    ok, args = run_extended_parser()
    if ok:
        dispatch_extended(args)
        return
    
    print_help(error=True)
