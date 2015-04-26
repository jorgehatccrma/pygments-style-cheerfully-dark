#!/usr/bin/python

from setuptools import setup

setup(
    name = 'pygments-style-cheerfully-dark',
    version = '0.1',
    description = 'Pygments version of the "Cheerfully Dark" Sublime Text theme.',
    license = 'BSD',

    author = 'Jorge Herrera',
    author_email = 'jherreras@gmail.com',

    url = 'https://github.com/jorgehatccrma/pygments-style-cheerfully-dark',

    packages = ['pygments_style_cheerfully_dark'],
    install_requires = ['pygments >= 1.4'],

    entry_points = '''[pygments.styles]
                      cheerfully_dark = pygments_style_cheerfully_dark:CheerfullyDarkStyle''',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)