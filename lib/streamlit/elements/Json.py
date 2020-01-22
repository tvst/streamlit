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

# Python 2/3 compatibility
from __future__ import print_function, division, unicode_literals, absolute_import
from streamlit.compatibility import setup_2_3_shims

setup_2_3_shims(globals())

import json

from streamlit.elements import framework


class Json(framework.Element):
    """Display object or string as a pretty-printed JSON string.

    Parameters
    ----------
    body : Object or str
        The object to print as JSON. All referenced objects should be
        serializable to JSON as well. If object is a string, we assume it
        contains serialized JSON.

    Example
    -------
    >>> st.json({
    ...     'foo': 'bar',
    ...     'baz': 'boz',
    ...     'stuff': [
    ...         'stuff 1',
    ...         'stuff 2',
    ...         'stuff 3',
    ...         'stuff 5',
    ...     ],
    ... })

    .. output::
       https://share.streamlit.io/0.25.0-2JkNY/index.html?id=CTFkMQd89hw3yZbZ4AUymS
       height: 280px

    """

    def __init__(self, body):
        super(Json, self).__init__()

        self._element.json.body = (
            body
            if isinstance(body, string_types)  # noqa: F821
            else json.dumps(body, default=lambda o: str(type(o)))
        )
