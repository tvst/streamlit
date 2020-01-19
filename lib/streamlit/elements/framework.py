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

from streamlit.proto import Element_pb2


class Element(object):
    def __init__(self):
        # These should be filled by subclasses. They are meant for internal
        # use in the Streamlit code, and not for use by users. They have been
        # prefixed with an underscore to make sure users don't accidentally
        # modify them.
        self._element = Element_pb2.Element()
        self._width = None
        self._height = None

        # Return value for widgets.
        self.value = NoValue


class NoValue(object):
    """Return this from DeltaGenerator.foo_widget() when you want the st.foo_widget()
    call to return None. This is needed because `_enqueue` replaces `None` with
    a `DeltaGenerator` (for use in non-widget elements).
    """

    pass
