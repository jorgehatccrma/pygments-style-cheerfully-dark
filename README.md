Pygment style based on [CheerfullyDark](https://github.com/jorgehatccrma/CheerfullyDark) Sublime Text Theme. The code is a modified version of [pygments-style-railscasts](https://github.com/DrMegahertz/pygments-style-railscasts).

Installation:
=============

Using PyPI and pip:

    pip install pygments-style-cheerfully-dark

Manual installation:

    git clone git://github.com/jorgehatccrma/pygments-style-cheerfully-dark.git
    cd pygments-style-cheerfully-dark
    python setup.py install


Usage example:
==============

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='cheerfully_dark').style
    <class 'pygments_style_cheerfully_dark:CheerfullyDarkStyle'>


Export the style as CSS:
========================

    pygmentize -S cheerfully_dark -f html > cheerfully-dark.css


Please read the [official documentation][pygments] for further information
on the usage of pygment styles.


For development
===============

To generate a CSS file, for example to use with `pelican-bootstrap3`, run

    pygmentize -S cheerfully_dark -f html > cheerfully_dark.css



[pygments]: http://pygments.org/docs/