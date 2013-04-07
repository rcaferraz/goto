# coding: utf-8
import sys
import os
import argparse
from storage import Storage, LabelAlreadyExistsError, LabelTooLongError, LABEL_SIZE


storage = Storage()


def remove(label):
    try:
        storage.remove(label)
        print '%s label was removed.' % label
    except:
        sys.stderr.write('%s is not a valid label.\n' % label)
        sys.exit(1)


def replace(label, path):
    try:
        storage.replace(label, path)
        print '%s label now points to %s.' % (label, path)
    except LabelTooLongError:
        sys.stderr.write('%s is too long. The size limit is %d characters.\n'
                                                        % (label, LABEL_SIZE))
        sys.exit(1)


def add(label, path):
    try:
        storage.add(label, path)
        print '%s label points to %s.' % (label, path)
    except LabelAlreadyExistsError:
        sys.stderr.write('%s label already exists. Use --replace.\n' % label)
        sys.exit(1)
    except LabelTooLongError:
        sys.stderr.write('%s is too long. The size limit is %d characters.\n'
                                                        % (label, LABEL_SIZE))
        sys.exit(1)


def main():
    """Entrypoint for the `label` utility."""
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.set_defaults(mode='insert')
    group.add_argument('--remove', action='store_const', dest='mode',
                            const='remove', help='remove an existing label')
    group.add_argument('--replace', action='store_const', dest='mode',
                            const='replace', help='replace an existing label')
    group.add_argument('--insert', action='store_const', dest='mode',
                                    const='insert', help='insert a new label')
    parser.add_argument('label', nargs='?', help='name of the label')
    args = parser.parse_args()

    if not args.label and args.mode in ['remove', 'replace']:
        parser.error('can\'t %s without specify a label.' % args.mode)

    curr_dir = os.getcwd()
    storage.open_or_create()

    if args.mode == 'remove':
        remove(args.label)

    elif args.mode == 'replace':
        replace(args.label, curr_dir)

    else:
        if not args.label:
            args.label = curr_dir[curr_dir.rfind('/')+1:]

        add(args.label, curr_dir)
