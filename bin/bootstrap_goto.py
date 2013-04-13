#!/usr/bin/env python
import sys
from goto import core
from goto import label


def bootstrap():
    # Remove bootstrap-like string from argv
    del sys.argv[0]

    if 'label' in sys.argv[0]:
        return label.main()
    elif 'goto' in sys.argv[0]:
        return core.main()
    sys.exit(-1)


if __name__ == '__main__':
    bootstrap()
