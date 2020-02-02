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

"""Streamlit.

How to use Streamlit in 3 seconds:

    1. Write an app
    >>> import streamlit as st
    >>> st.write(anything_you_want)

    2. Run your app
    $ streamlit run my_script.py

    3. Use your app
    A new tab will open on your browser. That's your Streamlit app!

    4. Modify your code, save it, and watch changes live on your browser.

Take a look at the other commands in this module to find out what else
Streamlit can do:

    >>> dir(streamlit)

Or try running our "Hello World":

    $ streamlit hello

For more detailed info, see https://docs.streamlit.io.
"""

# IMPORTANT: Prefix with an underscore anything that the user shouldn't see.

# NOTE: You'll see lots of "noqa: F821" in this file. That's because we
# manually mess with the local namespace so the linter can't know that some
# identifiers actually exist in the namespace.

# Python 2/3 compatibility
from __future__ import print_function, division, unicode_literals, absolute_import
from streamlit.compatibility import (
    setup_2_3_shims as _setup_2_3_shims,
    is_running_py3 as _is_running_py3,
)

_setup_2_3_shims(globals())

# Must be at the top, to avoid circular dependency.
from streamlit import logger as _logger
from streamlit import config as _config

_LOGGER = _logger.get_logger("root")

# Give the package a version.
import pkg_resources as _pkg_resources
import uuid as _uuid
import subprocess
import platform
import os

# This used to be pkg_resources.require('streamlit') but it would cause
# pex files to fail. See #394 for more details.
__version__ = _pkg_resources.get_distribution("streamlit").version

# Deterministic Unique Streamlit User ID
# The try/except is needed for python 2/3 compatibility
try:

    if (
        platform.system() == "Linux"
        and os.path.isfile("/etc/machine-id") == False
        and os.path.isfile("/var/lib/dbus/machine-id") == False
    ):
        print("Generate machine-id")
        subprocess.run(["sudo", "dbus-uuidgen", "--ensure"])

    machine_id = _uuid.getnode()
    if os.path.isfile("/etc/machine-id"):
        with open("/etc/machine-id", "r") as f:
            machine_id = f.read()
    elif os.path.isfile("/var/lib/dbus/machine-id"):
        with open("/var/lib/dbus/machine-id", "r") as f:
            machine_id = f.read()

    __installation_id__ = str(_uuid.uuid5(_uuid.NAMESPACE_DNS, str(machine_id)))

except UnicodeDecodeError:
    __installation_id__ = str(
        _uuid.uuid5(_uuid.NAMESPACE_DNS, str(_uuid.getnode()).encode("utf-8"))
    )

import contextlib as _contextlib
import re as _re
import sys as _sys
import textwrap as _textwrap
import threading as _threading
import traceback as _traceback
import json as _json
import numpy as _np

from streamlit import code_util as _code_util
from streamlit import env_util as _env_util
from streamlit import source_util as _source_util
from streamlit import string_util as _string_util
from streamlit import type_util as _type_util
from streamlit.Container import Container as _Container
from streamlit.ReportThread import add_report_ctx as _add_report_ctx
from streamlit.ReportThread import get_report_ctx as _get_report_ctx
from streamlit.errors import StreamlitAPIException
from streamlit.proto import BlockPath_pb2 as _BlockPath_pb2
from streamlit.util import functools_wraps as _functools_wraps

# Modules that the user should have access to.
from streamlit.caching import cache  # noqa: F401
import streamlit.elements as elements  # noqa: F401

# This is set to True inside cli._main_run(), and is False otherwise.
# If False, we should assume that Container functions are effectively
# no-ops, and adapt gracefully.
_is_running_with_streamlit = False


def _set_log_level():
    _logger.set_log_level(_config.get_option("global.logLevel").upper())
    _logger.init_tornado_logs()


# Make this file only depend on config option in an asynchronous manner. This
# avoids a race condition when another file (such as a test file) tries to pass
# in an alternative config.
_config.on_config_parsed(_set_log_level)

main = _Container(container=_BlockPath_pb2.BlockPath.MAIN)
sidebar = _Container(container=_BlockPath_pb2.BlockPath.SIDEBAR)

altair_chart = main.altair_chart  # noqa: E221
area_chart = main.area_chart  # noqa: E221
audio = main.audio  # noqa: E221
bar_chart = main.bar_chart  # noqa: E221
code = main.code  # noqa: E221
empty = main.empty  # noqa: E221
error = main.error  # noqa: E221
header = main.header  # noqa: E221
image = main.image  # noqa: E221
info = main.info  # noqa: E221
latex = main.latex  # noqa: E221
line_chart = main.line_chart  # noqa: E221
markdown = main.markdown  # noqa: E221
subheader = main.subheader  # noqa: E221
success = main.success  # noqa: E221
text = main.text  # noqa: E221
title = main.title  # noqa: E221
video = main.video  # noda: E221
warning = main.warning  # noqa: E221
write = main.write  # noqa: E221
balloons = main.balloons  # noqa: E221
progress = main.progress  # noqa: E221
json = main.json  # noqa: E221
exception = main.exception  # noqa: E221
help = main.help  # noqa: E221
# vega_lite_chart

# text_input
# text_area
# multiselect
# number_input
# radio
# selectbox
# slider
# time_input
# button
# checkbox
# date_input

# file_uploader

# dataframe = _with_ctr(_Container.dataframe)  # noqa: E221
# table = _with_ctr(_Container.table)  # noqa: E221

# bokeh_chart = _with_ctr(_Container.bokeh_chart)  # noqa: E221
# deck_gl_chart = _with_ctr(_Container.deck_gl_chart)  # noqa: E221
# pydeck_chart = _with_ctr(_Container.pydeck_chart)  # noqa: E221
# graphviz_chart = _with_ctr(_Container.graphviz_chart)  # noqa: E221
# map = _with_ctr(_Container.map)  # noqa: E221
# plotly_chart = _with_ctr(_Container.plotly_chart)  # noqa: E221
# pyplot = _with_ctr(_Container.pyplot)  # noqa: E221

get_option = _config.get_option


def set_option(key, value):
    """Set config option.

    Currently, only two config options can be set within the script itself:
        * client.caching
        * client.displayEnabled

    Calling with any other options will raise StreamlitAPIException.

    Run `streamlit config show` in the terminal to see all available options.

    Parameters
    ----------
    key : str
        The config option key of the form "section.optionName". To see all
        available options, run `streamlit config show` on a terminal.

    value
        The new value to assign to this config option.

    """
    opt = _config._config_options[key]
    if opt.scriptable:
        _config.set_option(key, value)
        return

    raise StreamlitAPIException(
        "{key} cannot be set on the fly. Set as command line option, e.g. streamlit run script.py --{key}, or in config.toml instead.".format(
            key=key
        )
    )


# Special methods:


def show(*args):
    """Write arguments to your app for debugging purposes.

    Show() has similar properties to write():

        1. You can pass in multiple arguments, all of which will be debugged.
        2. It returns None, so it's "slot" in the app cannot be reused.

    Parameters
    ----------
    *args : any
        One or many objects to debug in the App.

    Example
    -------

    >>> dataframe = pd.DataFrame({
    ...     'first column': [1, 2, 3, 4],
    ...     'second column': [10, 20, 30, 40],
    ... }))
    >>> st.show(dataframe)

    Notes
    -----
    This is an experimental feature with usage limitations.

    - The method must be called with the name `show`
    - Must be called in one line of code, and only once per line
    - When passing multiple arguments the inclusion of `,` or `)` in a string
    argument may cause an error.

    """
    if not args:
        return

    try:
        import inspect

        # Get the calling line of code
        previous_frame = inspect.currentframe().f_back
        lines = inspect.getframeinfo(previous_frame)[3]

        if not lines:
            warning("`show` not enabled in the shell")
            return

        # Parse arguments from the line
        line = lines[0].split("show", 1)[1]
        inputs = _code_util.get_method_args_from_code(args, line)

        # Escape markdown and add deltas
        for idx, input in enumerate(inputs):
            escaped = _string_util.escape_markdown(input)

            markdown("**%s**" % escaped)
            write(args[idx])

    except Exception:
        _, exc, exc_tb = _sys.exc_info()
        exception(exc, exc_tb)  # noqa: F821


@_contextlib.contextmanager
def spinner(text="In progress..."):
    """Temporarily displays a message while executing a block of code.

    Parameters
    ----------
    text : str
        A message to display while executing that block

    Example
    -------

    >>> with st.spinner('Wait for it...'):
    >>>     time.sleep(5)
    >>> st.success('Done!')

    """
    import streamlit.caching as caching

    display_message_lock = None

    # @st.cache optionally uses spinner for long-running computations.
    # Normally, streamlit warns the user when they call st functions
    # from within an @st.cache'd function. But we do *not* want to show
    # these warnings for spinner's message, so we create and mutate this
    # message delta within the "suppress_cached_st_function_warning"
    # context.
    with caching.suppress_cached_st_function_warning():
        message = empty()

    try:
        # Set the message 0.1 seconds in the future to avoid annoying
        # flickering if this spinner runs too quickly.
        DELAY_SECS = 0.1
        display_message = True
        display_message_lock = _threading.Lock()

        def set_message():
            with display_message_lock:
                if display_message:
                    with caching.suppress_cached_st_function_warning():
                        message.warning(str(text))

        _add_report_ctx(_threading.Timer(DELAY_SECS, set_message)).start()

        # Yield control back to the context.
        yield
    finally:
        if display_message_lock:
            with display_message_lock:
                display_message = False
        with caching.suppress_cached_st_function_warning():
            message.empty()


_SPACES_RE = _re.compile("\\s*")


@_contextlib.contextmanager
def echo():
    """Use in a `with` block to draw some code on the app, then execute it.

    Example
    -------

    >>> with st.echo():
    >>>     st.write('This code will be printed')

    """
    code = empty()  # noqa: F821
    try:
        frame = _traceback.extract_stack()[-3]
        if _is_running_py3():
            filename, start_line = frame.filename, frame.lineno
        else:
            filename, start_line = frame[:2]
        yield
        frame = _traceback.extract_stack()[-3]
        if _is_running_py3():
            end_line = frame.lineno
        else:
            end_line = frame[1]
        lines_to_display = []
        with _source_util.open_python_file(filename) as source_file:
            source_lines = source_file.readlines()
            lines_to_display.extend(source_lines[start_line:end_line])
            initial_spaces = _SPACES_RE.match(lines_to_display[0]).end()
            for line in source_lines[end_line:]:
                indentation = _SPACES_RE.match(line).end()
                # The != 1 is because we want to allow '\n' between sections.
                if indentation != 1 and indentation < initial_spaces:
                    break
                lines_to_display.append(line)
        lines_to_display = _textwrap.dedent("".join(lines_to_display))
        code.code(lines_to_display, "python")

    except FileNotFoundError as err:  # noqa: F821
        code.warning("Unable to display code. %s" % err)


def _transparent_write(*args):
    """This is just st.write, but returns the arguments you passed to it."""
    write(*args)
    if len(args) == 1:
        return args[0]
    return args


# We want to show a warning when the user runs a Streamlit script without
# 'streamlit run', but we need to make sure the warning appears only once no
# matter how many times __init__ gets loaded.
_repl_warning_has_been_displayed = False


def _maybe_print_repl_warning():
    global _repl_warning_has_been_displayed

    if not _repl_warning_has_been_displayed:
        _repl_warning_has_been_displayed = True

        if _env_util.is_repl():
            _LOGGER.warning(
                _textwrap.dedent(
                    """

                Will not generate Streamlit app

                  To generate an app, use Streamlit in a file and run it with:
                  $ streamlit run [FILE_NAME] [ARGUMENTS]

                """
                )
            )

        elif _config.get_option("global.showWarningOnDirectExecution"):
            script_name = _sys.argv[0]

            _LOGGER.warning(
                _textwrap.dedent(
                    """

                Will not generate Streamlit App

                  To generate an App, run this file with:
                  $ streamlit run %s [ARGUMENTS]

                """
                ),
                script_name,
            )
