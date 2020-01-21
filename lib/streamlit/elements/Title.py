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


class Title(framework.Element):
    """Display text in title formatting.

    Each document should have a single `st.title()`, although this is not
    enforced.

    Parameters
    ----------
    body : str
        The text to display.

    Example
    -------
    >>> st.title('This is a title')

    ...or:

    >>> el = st.Title('This is a title')
    >>> st.write(el)

    .. output::
       https://share.streamlit.io/0.25.0-2JkNY/index.html?id=SFcBGANWd8kWXF28XnaEZj
       height: 100px

    """

    def __init__(self, body, unsafe_allow_html=False):
        super(Title, self).__init__()
        self._element.markdown.body = "# %s" % clean_text(body)
