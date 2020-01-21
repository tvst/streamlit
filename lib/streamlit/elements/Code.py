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


class Code(framework.Element):
    """Display a code block with optional syntax highlighting.

    (This is a convenience wrapper around `st.markdown()`)

    Parameters
    ----------
    body : str
        The string to display as code.

    language : str
        The language that the code is written in, for syntax highlighting.
        If omitted, the code will be unstyled.

    Example
    -------
    >>> code = '''def hello():
    ...     print("Hello, Streamlit!")'''
    >>> st.code(code, language='python')

    .. output::
       https://share.streamlit.io/0.27.0-kBtt/index.html?id=VDRnaCEZWSBCNUd5gNQZv2
       height: 100px

    """

    def __init__(self, body, language="python"):
        super(Code, self).__init__()
        markdown = "```%(language)s\n%(body)s\n```" % {
            "language": language or "",
            "body": body,
        }
        self._element.markdown.body = clean_text(markdown)
