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


class Header(framework.Element):
    """Display text in header formatting.

    Parameters
    ----------
    body : str
        The text to display.

    Example
    -------
    >>> st.header('This is a header')

    ...or:

    >>> el = st.Header('This is a header')
    >>> st.write(el)

    .. output::
       https://share.streamlit.io/0.25.0-2JkNY/index.html?id=AnfQVFgSCQtGv6yMUMUYjj
       height: 100px

    """

    def __init__(self, body):
        super(Header, self).__init__()
        self._element.markdown.body = "## %s" % clean_text(body)
