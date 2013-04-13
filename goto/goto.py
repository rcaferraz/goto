# coding: utf-8
import os
import sys
import locale
import argparse
import comm
from exception import warning_and_exit
from storage import Storage, NoOptionError, LABEL_SIZE


lang, enc = locale.getdefaultlocale()
storage = Storage()
storage.open_or_create()


def format_label(label):
    return label + (LABEL_SIZE - len(label)) * u' '


def list_all_labels():
    """Prints all labels and its associated paths."""
    labels = storage.get_all()
    for label, path in labels.iteritems():
        s = u'%s %s' % (format_label(label), path)
        print s.encode(enc)


def change_directory(label):
    """Writes into the exchange file the path to goto."""
    try:
        path = storage.get(label)
        if not os.path.isdir(path):
            raise DanglingLabelError()

        comm.send(comm.PATH, path, enc)

    except NoOptionError:
        warning_and_exit('%s is not a valid label.' % label)

    except DanglingLabelError:
        storage.remove(label)
        warning_and_exit('%s is not a valid path. label %s was removed.'
            % (path, label))


def dispatch(label):
    """"""
    if label:
        label = unicode(label, enc)
        change_directory(label)
    else:
        list_all_labels()


class DanglingLabelError(Exception):
    pass
