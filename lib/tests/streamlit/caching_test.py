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

"""st.caching unit tests."""
import threading
import unittest
import pytest

from mock import patch

import streamlit as st
from streamlit import caching
from tests import testutil


class CacheTest(testutil.DeltaGeneratorTestCase):
    def tearDown(self):
        # Some of these tests reach directly into _cache_info and twiddle it.
        # Reset default values on teardown.
        st.caching._cache_info.within_cached_func = 0
        st.caching._cache_info.suppress_st_function_warning = 0

    def test_simple(self):
        @st.cache
        def foo():
            return 42

        self.assertEqual(foo(), 42)
        self.assertEqual(foo(), 42)

    def test_deprecated_kwarg(self):
        with pytest.raises(Exception) as e:

            @st.cache(ignore_hash=True)
            def foo():
                return 42

        assert (
            "The `ignore_hash` argument has been renamed to `allow_output_mutation`."
            in str(e.value)
        )

    @patch.object(st, "warning")
    def test_args(self, warning):
        called = [False]

        @st.cache
        def f(x):
            called[0] = True
            return x

        self.assertFalse(called[0])
        f(0)

        self.assertTrue(called[0])

        called = [False]  # Reset called

        f(0)
        self.assertFalse(called[0])

        f(1)
        self.assertTrue(called[0])

        warning.assert_not_called()

    @patch.object(st, "warning")
    def test_mutate_return(self, warning):
        @st.cache
        def f():
            return [0, 1]

        r = f()

        r[0] = 1

        warning.assert_not_called()

        r2 = f()

        warning.assert_called()

        self.assertEqual(r, r2)

    @patch.object(st, "warning")
    def test_mutate_args(self, warning):
        @st.cache
        def foo(d):
            d["answer"] += 1
            return d["answer"]

        d = {"answer": 0}

        self.assertNotEqual(foo(d), foo(d))

        warning.assert_not_called()

    @patch("streamlit.caching._show_cached_st_function_warning")
    def test_cached_st_function_warning(self, warning):
        st.text("foo")
        warning.assert_not_called()

        @st.cache
        def cached_func():
            st.text("Inside cached func")

        cached_func()
        warning.assert_called_once()

        warning.reset_mock()

        # Make sure everything got reset properly
        st.text("foo")
        warning.assert_not_called()

        # Test warning suppression
        @st.cache(suppress_st_warning=True)
        def suppressed_cached_func():
            st.text("No warnings here!")

        suppressed_cached_func()

        warning.assert_not_called()

        # Test nested st.cache functions
        @st.cache
        def outer():
            @st.cache
            def inner():
                st.text("Inside nested cached func")

            return inner()

        outer()
        warning.assert_called_once()

        warning.reset_mock()

        # Test st.cache functions that raise errors
        with self.assertRaises(RuntimeError):

            @st.cache
            def cached_raise_error():
                st.text("About to throw")
                raise RuntimeError("avast!")

            cached_raise_error()

        warning.assert_called_once()
        warning.reset_mock()

        # Make sure everything got reset properly
        st.text("foo")
        warning.assert_not_called()

        # Test st.cache functions with widgets
        @st.cache
        def cached_widget():
            st.button("Press me!")

        cached_widget()

        warning.assert_called_once()
        warning.reset_mock()

        # Make sure everything got reset properly
        st.text("foo")
        warning.assert_not_called()

    def test_caching_counter(self):
        """Test that _within_cached_function_counter behaves properly in
        multiple threads."""

        def get_counter():
            return caching._cache_info.within_cached_func

        def set_counter(val):
            caching._cache_info.within_cached_func = val

        self.assertEqual(0, get_counter())
        set_counter(1)
        self.assertEqual(1, get_counter())

        values_in_thread = []

        def thread_test():
            values_in_thread.append(get_counter())
            set_counter(55)
            values_in_thread.append(get_counter())

        thread = threading.Thread(target=thread_test)
        thread.start()
        thread.join()

        self.assertEqual([0, 55], values_in_thread)

        # The other thread should not have modified the main thread
        self.assertEqual(1, get_counter())


# Temporarily turn off these tests since there's no Cache object in __init__
# right now.
class CachingObjectTest(unittest.TestCase):
    def off_test_simple(self):
        val = 42

        for _ in range(2):
            c = st.Cache()
            if c:
                c.value = val

            self.assertEqual(c.value, val)

    def off_test_allow_output_mutation(self):
        val = 42

        for _ in range(2):
            c = st.Cache(allow_output_mutation=True)
            if c:
                c.value = val

            self.assertEqual(c.value, val)

    def off_test_has_changes(self):
        val = 42

        for _ in range(2):
            c = st.Cache()
            if c.has_changes():
                c.value = val

            self.assertEqual(c.value, val)

    @patch.object(st, "warning")
    def off_test_mutate(self, warning):
        for _ in range(2):
            c = st.Cache()
            if c:
                c.value = [0, 1]

            c.value[0] = 1

        warning.assert_called()
