from datetime import date

import pandas as pd
import streamlit as st

df = pd.DataFrame(
    {
        "index": [
            date(2019, 8, 9),
            date(2019, 8, 10),
            date(2019, 8, 11),
            date(2019, 8, 12),
        ],
        "numbers": [10, 50, 30, 40],
    }
)

df.set_index("index", inplace=True)

# st.area/bar/line_chart all use Altair/Vega-Lite under the hood.
# By default, Vega-Lite displays time values in the browser's local
# time zone. In `altair.generate_chart`, we explicitly set the time
# display to UTC, so that our results are consistent. This test verifies
# that change!
st.area_chart(df)
st.bar_chart(df)
st.line_chart(df)
