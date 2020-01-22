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

import random

from streamlit.elements import framework
from streamlit.proto import Balloons_pb2


class Balloons(framework.Element):
    """Draw celebratory balloons.

    Example
    -------
    >>> st.balloons()

    ...then watch your app and get ready for a celebration!

    """

    def __init__(self):
        super(Balloons, self).__init__()
        self._element.balloons.type = Balloons_pb2.Balloons.DEFAULT
        self._element.balloons.execution_id = random.randrange(0xFFFFFFFF)
