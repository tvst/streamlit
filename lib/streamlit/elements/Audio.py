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


class Audio(framework.Element):
    """Display an audio player.

    Parameters
    ----------
    data : str, bytes, BytesIO, numpy.ndarray, or file opened with
            io.open().
        Raw audio data or a string with a URL pointing to the file to load.
        If passing the raw data, this must include headers and any other bytes
        required in the actual file.
    start_time: int
        The time from which this element should start playing.
    format : str
        The mime type for the audio file. Defaults to 'audio/wav'.
        See https://tools.ietf.org/html/rfc4281 for more info.

    Example
    -------
    >>> audio_file = open('myaudio.ogg', 'rb')
    >>> audio_bytes = audio_file.read()
    >>>
    >>> st.audio(audio_bytes, format='audio/ogg')

    .. output::
       https://share.streamlit.io/0.25.0-2JkNY/index.html?id=Dv3M9sA7Cg8gwusgnVNTHb
       height: 400px

    """
    def __init__(self, data, format="audio/wav", start_time=0):
        # TODO: Provide API to convert raw NumPy arrays to audio file (with
        # proper headers, etc)?
        from streamlit.elements import media_proto

        super(Audio, self).__init__()
        media_proto.marshall_audio(self._element.audio, data, format, start_time)
