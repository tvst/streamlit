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

from streamlit.string_util import clean_text
from streamlit.elements import framework


class Markdown(framework.Element):
    """Display string formatted as Markdown.

    Parameters
    ----------
    body : str
        The string to display as Github-flavored Markdown. Syntax
        information can be found at: https://github.github.com/gfm.

        This also supports:

        * Emoji shortcodes, such as `:+1:`  and `:sunglasses:`.
          For a list of all supported codes,
          see https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json.

        * LaTeX expressions, by just wrapping them in "$" or "$$" (the "$$"
          must be on their own lines). Supported LaTeX functions are listed
          at https://katex.org/docs/supported.html.

    unsafe_allow_html : bool
        By default, any HTML tags found in the body will be escaped and
        therefore treated as pure text. This behavior may be turned off by
        setting this argument to True.

        That said, we *strongly advise against it*. It is hard to write
        secure HTML, so by using this argument you may be compromising your
        users' security. For more information, see:

        https://github.com/streamlit/streamlit/issues/152

        *Also note that `unsafe_allow_html` is a temporary measure and may
        be removed from Streamlit at any time.*

        If you decide to turn on HTML anyway, we ask you to please tell us
        your exact use case here:

        https://discuss.streamlit.io/t/96

        This will help us come up with safe APIs that allow you to do what
        you want.

    Example
    -------
    >>> st.markdown('Streamlit is **_really_ cool**.')

    .. output::
       https://share.streamlit.io/0.25.0-2JkNY/index.html?id=PXz9xgY8aB88eziDVEZLyS
       height: 50px

    """

    def __init__(self, body, unsafe_allow_html=False):
        super(Markdown, self).__init__()
        self._element.markdown.body = clean_text(body)
        self._element.markdown.allow_html = unsafe_allow_html
