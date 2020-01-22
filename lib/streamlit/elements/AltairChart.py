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

from datetime import date

import altair as alt
import pandas as pd

from streamlit import type_util
from streamlit.elements import framework
import streamlit.elements.vega_lite as vega_lite


class AltairChart(framework.Element):
    """Display a chart using the Altair library.

    Parameters
    ----------
    altair_chart : altair.vegalite.v2.api.Chart
        The Altair chart object to display.

    width : number
        Deprecated. If != 0 (default), will show an alert.
        From now on you should set the width directly in the Altair
        spec. Please refer to the Altair documentation for details.

    use_container_width : bool
        If True, set the chart width to the column width. This takes
        precedence over Altair's native `width` value.

    Example
    -------

    >>> import pandas as pd
    >>> import numpy as np
    >>> import altair as alt
    >>>
    >>> df = pd.DataFrame(
    ...     np.random.randn(200, 3),
    ...     columns=['a', 'b', 'c'])
    ...
    >>> c = alt.Chart(df).mark_circle().encode(
    ...     x='a', y='b', size='c', color='c')
    >>>
    >>> st.altair_chart(c, width=-1)

    .. output::
       https://share.streamlit.io/0.25.0-2JkNY/index.html?id=8jmmXR8iKoZGV4kXaKGYV5
       height: 200px

    Examples of Altair charts can be found at
    https://altair-viz.github.io/gallery/.

    """

    def __init__(self, altair_chart, width=0, use_container_width=False):
        super(AltairChart, self).__init__()
        marshall(self._element, altair_chart, width, use_container_width)


def marshall(element, altair_chart, width=0, use_container_width=False):
    # Normally altair_chart.to_dict() would transform the dataframe used by the
    # chart into an array of dictionaries. To avoid that, we install a
    # transformer that replaces datasets with a reference by the object id of
    # the dataframe. We then fill in the dataset manually later on.

    datasets = {}

    def id_transform(data):
        """Altair data transformer that returns a fake named dataset with the
        object id."""
        datasets[id(data)] = data
        return {"name": str(id(data))}

    alt.data_transformers.register("id", id_transform)

    with alt.data_transformers.enable("id"):
        chart_dict = altair_chart.to_dict()

        # Put datasets back into the chart dict but note how they weren't
        # transformed.
        chart_dict["datasets"] = datasets

        vega_lite.marshall(
            element.vega_lite_chart,
            data=None,
            spec=chart_dict,
            use_container_width=use_container_width,
        )


def _is_date_column(df, name):
    """True if the column with the given name stores datetime.date values.

    This function just checks the first value in the given column, so
    it's meaningful only for columns whose values all share the same type.

    Parameters
    ----------
    df : pd.DataFrame
    name : str
        The column name

    Returns
    -------
    bool

    """
    column = df[name]
    if column.size == 0:
        return False
    return isinstance(column[0], date)


# TODO: Move this into a separate StreamlitChart module?
def generate_chart(chart_type, data, width=0, height=0):
    if data is None:
        # Use an empty-ish dict because if we use None the x axis labels rotate
        # 90 degrees. No idea why. Need to debug.
        data = {"": []}

    if not isinstance(data, pd.DataFrame):
        data = type_util.convert_anything_to_df(data)

    index_name = data.index.name
    if index_name is None:
        index_name = "index"

    data = pd.melt(data.reset_index(), id_vars=[index_name])

    if chart_type == "area":
        opacity = {"value": 0.7}
    else:
        opacity = {"value": 1.0}

    # Set the X and Y axes' scale to "utc" if they contain date values.
    # This causes time data to be displayed in UTC, rather the user's local
    # time zone. (By default, vega-lite displays time data in the browser's
    # local time zone, regardless of which time zone the data specifies:
    # https://vega.github.io/vega-lite/docs/timeunit.html#output).
    x_scale = (
        alt.Scale(type="utc") if _is_date_column(data, index_name) else alt.Undefined
    )
    y_scale = alt.Scale(type="utc") if _is_date_column(data, "value") else alt.Undefined

    chart = (
        getattr(alt.Chart(data, width=width, height=height), "mark_" + chart_type)()
        .encode(
            alt.X(index_name, title="", scale=x_scale),
            alt.Y("value", title="", scale=y_scale),
            alt.Color("variable", title="", type="nominal"),
            alt.Tooltip([index_name, "value", "variable"]),
            opacity=opacity,
        )
        .interactive()
    )
    return chart