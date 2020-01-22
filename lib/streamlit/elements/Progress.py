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
from streamlit.errors import StreamlitAPIException


class Progress(framework.Element):
    """Display a progress bar.

    Parameters
    ----------
    value : int
        The percentage complete: 0 <= value <= 100

    Example
    -------
    Here is an example of a progress bar increasing over time:

    >>> import time
    >>>
    >>> my_bar = st.progress(0)
    >>>
    >>> for percent_complete in range(100):
    ...     my_bar.progress(percent_complete + 1)

    """

    def __init__(self, value):
        super(Progress, self).__init__()

        # Needed for python 2/3 compatibility
        value_type = type(value).__name__
        if value_type == "float":
            if 0.0 <= value <= 1.0:
                self._element.progress.value = int(value * 100)
            else:
                raise StreamlitAPIException(
                    "Progress Value has invalid value [0.0, 1.0]: %f" % value
                )
        elif value_type == "int":
            if 0 <= value <= 100:
                self._element.progress.value = value
            else:
                raise StreamlitAPIException(
                    "Progress Value has invalid value [0, 100]: %d" % value
                )
        else:
            raise StreamlitAPIException(
                "Progress Value has invalid type: %s" % value_type
            )
