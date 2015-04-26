# -*- coding: utf-8 -*-
"""
    cheerfully-dark
    ~~~~~~~~~~

    Port of the Cheerfully Dark color scheme for Sublime Text.

    Based upon the work of Marcus Fredriksson.

    :copyright: Copyright 2015 Jorge Herrera
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text


class CheerfullyDarkStyle(Style):
    """
    Port of the Cheerfully Dark color scheme for Sublime Text.
    """

    default_style = ''

    background_color = '#0C0C0C'
    highlight_color = '#6486AB'

    styles = {
        Comment:                'italic #7F8989',

        Error:                  '#D2A8A1',

        Keyword:                '#2EC310',
        Keyword.Namespace:      '#86bb1b',

        Name:                   '#E8E8E8',
        Name.Builtin:           '#FEFA35',
        Name.Builtin.Pseudo:    '#5597D6',
        Name.Class:             '#FB503F',
        Name.Constant:          '#5463FB',
        Name.Function:          '#FB503F',

        Number:                 '#5463FB',

        Operator:               '#86bb1b',

        String:                 '#EE9630',

        Text:                   '#E8E8E8',

    }