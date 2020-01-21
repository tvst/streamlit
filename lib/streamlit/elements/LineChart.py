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


class LineChart(framework.Element):
    """Display a line chart.

    This is just syntax-sugar around st.altair_chart. The main difference
    is this command uses the data's own column and indices to figure out
    the chart's spec. As a result this is easier to use for many "just plot
    this" scenarios, while being less customizable.

    Parameters
    ----------
    data : pandas.DataFrame, pandas.Styler, numpy.ndarray, Iterable, or dict
        Data to be plotted.

    width : int
        The chart width in pixels. If 0, selects the width automatically.

    height : int
        The chart width in pixels. If 0, selects the height automatically.

    use_container_width : bool
        If True, set the chart width to the column width. This takes
        precedence over the width argument.

    Example
    -------
    >>> chart_data = pd.DataFrame(
    ...     np.random.randn(20, 3),
    ...     columns=['a', 'b', 'c'])
    ...
    >>> st.line_chart(chart_data)

    .. output::
       https://share.streamlit.io/0.50.0-td2L/index.html?id=Pp65STuFj65cJRDfhGh4Jt
       height: 220px

    """

    def __init__(self, data=None, width=0, height=0, use_container_width=True):
        super(LineChart, self).__init__()
        from streamlit.elements.AltairChart import generate_chart, marshall

        altair_chart = generate_chart("line", data, width, height)
        marshall(
            self._element, altair_chart, use_container_width=use_container_width,
        )
