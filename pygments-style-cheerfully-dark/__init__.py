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

        Keyword:                '#86bb1b',
        Keyword.Reserved:       '#86bb1b',
        Keyword.Type:           '#C5AF75',

        Name:                   '#FB503F',
        Name.Attribute:         '#AC885B',
        Name.Builtin:           '#2EC310',
        Name.Builtin.Pseudo:    '#2EC310',
        Name.Class:             '#5597D6',
        Name.Constant:          '#5463FB',
        Name.Decorator:         '#EE9630',
        Name.Function:          '#FB503F',
        Name.Tag:               '#86BB1B',

        Number:                 '#5463FB',

        Operator:               '#86BB1B',
        Operator.Word:          '#86BB1B',

        Punctuation:            '#E8E8E8',

        String:                 '#EE9630',
        String.Escape:          '#EE9630',

        Text:                   '#E8E8E8',
    }