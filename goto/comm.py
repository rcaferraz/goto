# coding: utf-8

EXCHANGE_FILE = '/tmp/goto'
PATH = '<PATH>'


def send(category, message, encoding):
    """Sends `message` to `EXCHANGE_FILE`."""
    with open(EXCHANGE_FILE, 'w') as f:
        f.write(category + '\n')
        f.write(message.encode(encoding) + '\n')
