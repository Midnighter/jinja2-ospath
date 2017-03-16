# -*- coding: utf-8 -*-

# Copyright 2017 Moritz Emanuel Beber

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
