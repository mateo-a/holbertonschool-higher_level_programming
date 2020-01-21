#!/usr/bin/python3
"""

Class MyInt that inherits from int

"""


class MyInt(int):
    """
    Class MyInt that inherits from int an returns the
    result of == an != operators inverted.
    """
    def __eq__(self, other):
        """Overrides the default __eq__ implementation"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the default __ne__ implementation"""
        return super().__eq__(other)
