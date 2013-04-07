# coding: utf-8
import sys
import locale
import argparse
from storage import Storage, NoOptionError, LABEL_SIZE


storage = Storage()
language, encoding = locale.getdefaultlocale()


def format_label(label):
    return label + (LABEL_SIZE - len(label)) * u' '


def list_labels():
    labels = storage.get_all()
    for label, path in labels.iteritems():
        s = u'%s  %s' % (format_label(label), path)
        print s.encode(encoding)


def change_directory(label):
    try:
        path = storage.get(label)
        print '<PATH>'
        print path.encode(encoding)
    except NoOptionError:
        sys.stderr.write('%s is not a valid label.\n' % label)
        sys.exit(1)


def main():
    """Entrypoint for the `goto` utility."""
    parser = argparse.ArgumentParser()
    parser.add_argument('label', nargs='?', help='name of the label')

    args = parser.parse_args()

    storage.open_or_create()

    if args.label:
        label = unicode(args.label, encoding)
        change_directory(label)
    else:
        list_labels()
