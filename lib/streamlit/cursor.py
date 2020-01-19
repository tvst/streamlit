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

from streamlit.ReportThread import get_report_ctx


def get_container_cursor(container):
    ctx = get_report_ctx()

    if container in ctx.cursors:
        return ctx.cursors[container]

    cursor = RunningCursor()
    ctx.cursors[container] = cursor
    return cursor


class AbstractCursor(object):
    @property
    def index(self):
        return self._index

    @property
    def path(self):
        return self._path

    @property
    def is_locked(self):
        return self._is_locked

    def get_locked_cursor(self, element):
        raise NotImplementedError()


class RunningCursor(AbstractCursor):
    def __init__(self, path=()):
        """A pointer to a location in the app.

        Parameters
        ----------
        path: tuple of ints
          The full path of this cursor, consisting of the IDs of all ancestors. The
          0th item is the topmost ancestor.

        """
        self._is_locked = False
        self._index = 0
        self._path = path

    def get_locked_cursor(self, element):
        locked_cursor = LockedCursor(
            path=self._path,
            index=self._index,
            element=element,
        )

        self._index += 1

        return locked_cursor


class LockedCursor(AbstractCursor):
    def __init__(self, path=(), index=None, element=None):
        """A pointer to a location in the app.

        Parameters
        ----------
        path: tuple of ints
          The full path of this cursor, consisting of the IDs of all ancestors. The
          0th item is the topmost ancestor.
        index: int or None
        element: Element or None

        """
        self._is_locked = True
        self._index = index
        self._path = path
        self.element = element

    def get_locked_cursor(self, element):
        self.element = element
        return self
