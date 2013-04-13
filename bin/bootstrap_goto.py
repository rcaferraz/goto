#!/usr/bin/env python
import sys
from goto import dispatcher


def bootstrap():
    # Remove bootstrap-like string from argv
    del sys.argv[0]
    dispatcher.main()


if __name__ == '__main__':
    bootstrap()
