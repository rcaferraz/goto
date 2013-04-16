# coding: utf-8
import os
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
        if not os.path.isdir(path):
            raise DanglingLabelError()

        with open('/tmp/goto', 'w') as f:
            f.write('<PATH>\n')
            f.write(path.encode(encoding) + '\n')

    except NoOptionError:
        red = '\033[01;31m'
        native = '\033[m'
        sys.stderr.write(red + '%s' % label + native + ' is not a valid label.\n')
        sys.exit(1)

    except DanglingLabelError:
        storage.remove(label)
        sys.stderr.write('%s is not a valid path. label %s was removed.\n' %
            (path, label))
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


class DanglingLabelError(Exception):
    pass
