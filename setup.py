# coding: utf-8
from distutils.core import setup

setup(
    name='goto-dir',
    version='0.1.0',
    author='Paulo Borges',
    author_email='pauloborgesfilho@gmail.com',
    packages=['goto','goto.test'],
    scripts=['bin/bootstrap_goto.py', 'bin/goto.sh'],
    url='http://pypi.python.org/pypi/goto-dir/',
    license='See LICENSE.',
    description='easy\'n\'fast cd\'ing.',
    long_description=open('README.md').read(),
)