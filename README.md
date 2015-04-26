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
    >>> HtmlFormatter(style='cheerfully-dark').style
    <class 'pygments-style-cheerfully-dark:CheerfullyStyle'>


Export the style as CSS:
========================

    pygmentize -S cheerfully-dark -f html > cheerfully-dark.css


Please read the [official documentation][pygments] for further information
on the usage of pygment styles.


[pygments]: http://pygments.org/docs/