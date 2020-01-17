# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
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


class Text(framework.Element):
    def __init__(self, body):
        """Fixed-width preformatted text.

        Parameters
        ----------
        body : str
            The string to display.

        Example
        -------
        >>> st.text('This is some text.')

        or

        >>> t = st.elements.Text('This is some text.')
        >>> st.write(t)

        .. output::
            https://share.streamlit.io/0.25.0-2JkNY/index.html?id=PYxU1kee5ubuhGR11NsnT1
            height: 50px

        """
        super(Text, self).__init__()
        self.msg.delta.new_element.text.body = clean_text(body)
