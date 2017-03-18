# -*- coding: utf-8 -*-
import pytest
import tempfile
import os.path

from moeap.profiles import list_profiles


class TestKeychain(object):

    def test_list_profiles(self):
        profiles = list_profiles()

        for profile in profiles:
