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


class Empty(framework.Element):
    """Add a placeholder to the app.

    The placeholder can be filled any time by calling methods on the return
    value.

    Example
    -------
    >>> my_placeholder = st.empty()
    >>>
    >>> # Now replace the placeholder with some text:
    >>> my_placeholder.text("Hello world!")
    >>>
    >>> # And replace the text with an image:
    >>> my_placeholder.image(my_image_bytes)

    """

    def __init__(self):
        super(Empty, self).__init__()
        # The protobuf needs something to be set
        self._element.empty.unused = True
