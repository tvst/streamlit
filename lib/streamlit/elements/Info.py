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
from streamlit.proto import Alert_pb2
from streamlit.string_util import clean_text


class Info(framework.Element):
    """Display an informational message.

    Parameters
    ----------
    body : str
        The info text to display.

    Example
    -------
    >>> st.info('This is a purely informational message')

    """

    def __init__(self, body):
        super(Info, self).__init__()
        self._element.alert.body = clean_text(body)
        self._element.alert.format = Alert_pb2.Alert.INFO
