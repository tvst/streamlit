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

import os
import platform
import re
import sys
import uuid


system = platform.system()
IS_LINUX = system == "Linux"
IS_WINDOWS = system == "Windows"
IS_DARWIN = system == "Darwin"
IS_BSD = "BSD" in system
IS_LINUX_OR_BSD = IS_LINUX or IS_BSD


def is_pex():
    """Return if streamlit running in pex.

    Pex modifies sys.path so the pex file is the first path and that's
    how we determine we're running in the pex file.
    """
    if re.match(r".*pex$", sys.path[0]):
        return True
    return False


def is_repl():
    """Return True if running in the Python REPL."""
    import inspect

    root_frame = inspect.stack()[-1]
    filename = root_frame[1]  # 1 is the filename field in this tuple.

    if filename.endswith(os.path.join("bin", "ipython")):
        return True

    # <stdin> is what the basic Python REPL calls the root frame's
    # filename, and <string> is what iPython sometimes calls it.
    if filename in ("<stdin>", "<string>"):
        return True

    return False


def is_executable_in_path(name):
    """Check if executable is in OS path."""
    from distutils.spawn import find_executable

    return find_executable(name) is not None


def _get_actual_machine_id():
    """Deterministic machine-specific ID.

    Do not change this function lightly! It impacts our metrics.
    """

    machine_id = None

    # We special-case Linux here because Docker containers (which usually run Linux) often return
    # the same uuid.getnode() no matter where they're run, which messes up our metrics.
    # (It would be cleaner to only special-case Linux *containers*, but since this code has already
    # shipped it doesn't make sense to change it and break our metrics.)
    if IS_LINUX:
        try:
            if os.path.isfile("/etc/machine-id"):
                with open("/etc/machine-id", "r") as f:
                    machine_id = f.read()
                    # NOTE: File may be empty.

            if not machine_id and os.path.isfile("/var/lib/dbus/machine-id"):
                with open("/var/lib/dbus/machine-id", "r") as f:
                    machine_id = f.read()

            # In a perfect world, this would be the only "if" case here, but see comment above.
            if not machine_id and os.path.isfile("/proc/self/cgroup"):
                with open("/proc/self/cgroup", "r") as f:
                    first_line = f.readline()
                    # See https://forums.docker.com/t/get-a-containers-full-id-from-inside-of-itself/37237.
                    if "docker" in first_line or "lxc" in first_line:
                        machine_id = first_line

        except:
            # Do nothing. Fall back to getnode().
            pass

    if machine_id is None:
        machine_id = str(uuid.getnode())

    return machine_id


def _get_mangled_machine_id():
    """Get a deterministic unique ID for this machine, for use in out metrics.

    Do not change this function lightly! It impacts our metrics.
    """
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, _get_actual_machine_id()))


machine_id = _get_mangled_machine_id()
