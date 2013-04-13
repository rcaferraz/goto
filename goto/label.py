# coding: utf-8
import os
import re
import locale
import core
from exception import warning_and_exit
from storage import Storage, LabelAlreadyExistsError, LabelTooLongError
from storage import LabelInvalidFormatError, LABEL_SIZE


lang, enc = locale.getdefaultlocale()
storage = Storage()
storage.open_or_create()


def delete(label):
    try:
        storage.remove(label)
        print "%s label was deleted." % label
    except:
        warning_and_exit("%s is not a valid label." % label)


def replace(label, path):
    try:
        storage.replace(label, path)
        print "%s label now points to %s." % (label, path)
    except LabelTooLongError:
        warning_and_exit("%s is too long. The maximum length is %d."
                                                        % (label, LABEL_SIZE))
    except LabelInvalidFormatError:
        warning_and_exit("%s is not a valid label." % label)


def add(label, path):
    """"""
    try:
        storage.add(label, path)
        print "%s label points to %s." % (label, path)
    except LabelAlreadyExistsError:
        warning_and_exit("%s label already exists. Use update instead of add."
                                                                    % label)
    except LabelTooLongError:
        warning_and_exit("%s is too long. The maximum length is %d."
                                                        % (label, LABEL_SIZE))
    except LabelInvalidFormatError:
        warning_and_exit("%s is not a valid label." % label)


def dispatch(action, label, path):
    """"""
    if not label and action in ["rm", "update"]:
        core.print_help(True, "can't %s without specify a label." % action)

    if path:
        path = unicode(path, enc)
    else:
        path = unicode(os.getcwd(), enc)

    if label:
        label = unicode(label, enc)
    else:
        # Since the first if verifies if there is a label when the action is
        # "rm" or "update", so the only time this is executed is when action
        # is "add".
        label = re.sub(r'\s+', '_', path[path.rfind('/')+1:], flags=re.UNICODE)

    if action == "rm":
        delete(label)

    elif action == "update":
        replace(label, path)

    elif action == "add":
        add(label, path)
