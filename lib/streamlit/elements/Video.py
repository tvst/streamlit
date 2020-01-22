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


class Video(framework.Element):
    """Display a video player.

    Parameters
    ----------
    data : str, bytes, BytesIO, numpy.ndarray, or file opened with
            io.open().
        Raw video data or a string with a URL pointing to the video
        to load. Includes support for YouTube URLs.
        If passing the raw data, this must include headers and any other
        bytes required in the actual file.
    format : str
        The mime type for the video file. Defaults to 'video/mp4'.
        See https://tools.ietf.org/html/rfc4281 for more info.
    start_time: int
        The time from which this element should start playing.

    Example
    -------
    >>> video_file = open('myvideo.mp4', 'rb')
    >>> video_bytes = video_file.read()
    >>>
    >>> st.video(video_bytes)

    .. output::
       https://share.streamlit.io/0.25.0-2JkNY/index.html?id=Wba9sZELKfKwXH4nDCCbMv
       height: 600px

    """

    def __init__(self, data, format="video/mp4", start_time=0):
        # TODO: Provide API to convert raw NumPy arrays to video file (with
        # proper headers, etc)?
        from streamlit.elements import media_proto

        super(Video, self).__init__()
        media_proto.marshall_video(self._element.video, data, format, start_time)
