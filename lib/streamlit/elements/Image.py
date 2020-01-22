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


class Image(framework.Element):
    """Display an image or list of images.

    Parameters
    ----------
    image : numpy.ndarray, [numpy.ndarray], BytesIO, str, or [str]
        Monochrome image of shape (w,h) or (w,h,1)
        OR a color image of shape (w,h,3)
        OR an RGBA image of shape (w,h,4)
        OR a URL to fetch the image from
        OR a list of one of the above, to display multiple images.
    caption : str or list of str
        Image caption. If displaying multiple images, caption should be a
        list of captions (one for each image).
    width : int or None
        Image width. None means use the image width.
    use_column_width : bool
        If True, set the image width to the column width. This takes
        precedence over the `width` parameter.
    clamp : bool
        Clamp image pixel values to a valid range ([0-255] per channel).
        This is only meaningful for byte array images; the parameter is
        ignored for image URLs. If this is not set, and an image has an
        out-of-range value, an error will be thrown.
    channels : 'RGB' or 'BGR'
        If image is an nd.array, this parameter denotes the format used to
        represent color information. Defaults to 'RGB', meaning
        `image[:, :, 0]` is the red channel, `image[:, :, 1]` is green, and
        `image[:, :, 2]` is blue. For images coming from libraries like
        OpenCV you should set this to 'BGR', instead.
    format : 'JPEG' or 'PNG'
        This parameter specifies the image format to use when transferring
        the image data. Defaults to 'JPEG'.

    Example
    -------
    >>> from PIL import Image
    >>> image = Image.open('sunrise.jpg')
    >>>
    >>> st.image(image, caption='Sunrise by the mountains',
    ...          use_column_width=True)

    .. output::
       https://share.streamlit.io/0.25.0-2JkNY/index.html?id=YCFaqPgmgpEz7jwE4tHAzY
       height: 630px

    """

    # TODO: Make this accept files and strings/bytes as input.
    def __init__(
        self,
        image,
        caption=None,
        width=None,
        use_column_width=False,
        clamp=False,
        channels="RGB",
        format="JPEG",
    ):
        import streamlit.elements.image_proto as image_proto

        super(Image, self).__init__()

        if use_column_width:
            width = -2
        elif width is None:
            width = -1
        elif width <= 0:
            raise StreamlitAPIException("Image width must be positive.")
        image_proto.marshall_images(
            image, caption, width, self._element.imgs, clamp, channels, format
        )
