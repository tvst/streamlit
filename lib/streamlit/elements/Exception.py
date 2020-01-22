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


class Exception(framework.Element):
    """Display an exception.

    Parameters
    ----------
    exception : Exception
        The exception to display.
    exception_traceback : Exception Traceback or None
        If None or False, does not show display the trace. If True,
        tries to capture a trace automatically. If a Traceback object,
        displays the given traceback.

    Example
    -------
    >>> e = RuntimeError('This is an exception of type RuntimeError')
    >>> st.exception(e)

    """

    def __init__(self, exception, exception_traceback=None):
        import streamlit.elements.exception_proto as exception_proto

        super(Exception, self).__init__()
        exception_proto.marshall(
            self._element.exception, exception, exception_traceback
        )
