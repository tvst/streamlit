# -*- coding: utf-8 -*-
# Copyright 2018-2020 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from streamlit.elements import framework
from streamlit.string_util import clean_text
from streamlit import type_util


class Latex(framework.Element):
    # This docstring needs to be "raw" because of the backslashes in the
    # example below.
    r"""Display mathematical expressions formatted as LaTeX.

    Supported LaTeX functions are listed at
    https://katex.org/docs/supported.html.

    Parameters
    ----------
    body : str or SymPy expression
        The string or SymPy expression to display as LaTeX. If str, it's
        a good idea to use raw Python strings since LaTeX uses backslashes
        a lot.


    Example
    -------
    >>> st.latex(r'''
    ...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    ...     \sum_{k=0}^{n-1} ar^k =
    ...     a \left(\frac{1-r^{n}}{1-r}\right)
    ...     ''')

    .. output::
       https://share.streamlit.io/0.50.0-td2L/index.html?id=NJFsy6NbGTsH2RF9W6ioQ4
       height: 75px

    """

    def __init__(self, body):
        super(Latex, self).__init__()
        if type_util.is_sympy_expession(body):
            import sympy

            body = sympy.latex(body)

        self._element.markdown.body = "$$\n%s\n$$" % clean_text(body)
