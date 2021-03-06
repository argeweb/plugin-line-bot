# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""linebot.models.messages module."""

from __future__ import unicode_literals

from abc import ABCMeta

from argeweb.libs.six import with_metaclass

from .base import Base


class Message(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of Message."""

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param kwargs:
        """
        super(Message, self).__init__(**kwargs)

        self.type = None
        self.id = id


class TextMessage(Message):
    """TextMessage.

    https://devdocs.line.me/en/#text-message

    Message object which contains the text sent from the source.
    """

    def __init__(self, id=None, text=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str text: Message text
        :param kwargs:
        """
        super(TextMessage, self).__init__(id=id, **kwargs)

        self.type = 'text'
        self.text = text


class ImageMessage(Message):
    """ImageMessage.

    https://devdocs.line.me/en/#image-message

    Message object which contains the image content sent from the source.
    The binary image data can be retrieved with the Content API.
    """

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param kwargs:
        """
        super(ImageMessage, self).__init__(id=id, **kwargs)

        self.type = 'image'


class VideoMessage(Message):
    """VideoMessage.

    https://devdocs.line.me/en/#video-message

    Message object which contains the video content sent from the source.
    The binary video data can be retrieved with the Content API.
    """

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param kwargs:
        """
        super(VideoMessage, self).__init__(id=id, **kwargs)

        self.type = 'video'


class AudioMessage(Message):
    """AudioMessage.

    https://devdocs.line.me/en/#audio-message

    Message object which contains the audio content sent from the source.
    The binary audio data can be retrieved with the Content API.
    """

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param kwargs:
        """
        super(AudioMessage, self).__init__(id=id, **kwargs)

        self.type = 'audio'


class LocationMessage(Message):
    """LocationMessage.

    https://devdocs.line.me/en/#location-message
    """

    def __init__(self, id=None, title=None, address=None, latitude=None, longitude=None,
                 **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str title: Title
        :param str address: Address
        :param float latitude: Latitude
        :param float longitude: Longitude
        :param kwargs:
        """
        super(LocationMessage, self).__init__(id=id, **kwargs)

        self.type = 'location'
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


class StickerMessage(Message):
    """StickerMessage.

    https://devdocs.line.me/en/#sticker-message

    Message object which contains the sticker data sent from the source.
    For a list of basic LINE stickers and sticker IDs, see sticker list.
    """

    def __init__(self, id=None, package_id=None, sticker_id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str package_id: Package ID
        :param str sticker_id: Sticker ID
        :param kwargs:
        """
        super(StickerMessage, self).__init__(id=id, **kwargs)

        self.type = 'sticker'
        self.package_id = package_id
        self.sticker_id = sticker_id
