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

from streamlit.proto import ForwardMsg_pb2


class Element(object):
    def __init__(self):
        # Should be filled by subclasses. (TODO: Make this an Element.proto)
        self.msg = ForwardMsg_pb2.ForwardMsg()

        # Return value for widgets. (TODO: Make this pull from WidgetState)
        self.value = NoValue


class NoValue(object):
    """Return this from DeltaGenerator.foo_widget() when you want the st.foo_widget()
    call to return None. This is needed because `_enqueue` replaces `None` with
    a `DeltaGenerator` (for use in non-widget elements).
    """

    pass
