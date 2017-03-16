# -*- coding: utf-8 -*-

"""
Extensions that introduce `basename` and `dirname` as Jinja2 filters.

Examples
--------

    my_path = "/some/absolute/path/with/file.txt"
    {{ my_path | basename }}

Will fill in `file.txt`.
"""

from __future__ import absolute_import

import os.path

from jinja2.ext import Extension

__all__ = ("OSPathExtension",)


class OSPathExtension(Extension):
    """A Jinja2 extension that introduces `os.path` functionality."""

    tags = frozenset(["basename", "dirname"])

    def __init__(self, environment):
        """Initialize the extension and prepare the Jinja2 environment."""
        super(OSPathExtension, self).__init__(environment)
        for name in self.tags:
            environment.filters[name] = getattr(os.path, name)
