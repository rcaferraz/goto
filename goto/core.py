# coding: utf-8
import argparse
import goto


def main():
    """Entrypoint for the `goto` utility."""
    parser = argparse.ArgumentParser()
    parser.add_argument('label', nargs='?', help='name of the label')

    args = parser.parse_args()

    label = args.label or None
    goto.dispatch(args.label)
