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


class Help(framework.Element):
    """Display object's doc string, nicely formatted.

    Displays the doc string for this object.

    Parameters
    ----------
    obj : Object
        The object whose docstring should be displayed.

    Example
    -------

    Don't remember how to initialize a dataframe? Try this:

    >>> st.help(pandas.DataFrame)

    Want to quickly check what datatype is output by a certain function?
    Try:

    >>> x = my_poorly_documented_function()
    >>> st.help(x)

    """

    def __init__(self, obj):
        import streamlit.elements.doc_string as doc_string

        super(Help, self).__init__()
        doc_string.marshall(self._element, obj)
