"""
lverweijen startup file
"""

import importlib

class ModuleProxy(object):
    """A proxy for importing modules lazily."""

    __slots__ = ("_module_name", "_module_package", "_module_alias")

    def __init__(self, name, package=None, alias=None):
        """Initialize a lazy module."""
        object.__setattr__(self, '_module_name', name)
        object.__setattr__(self, '_module_package', package)
        object.__setattr__(self, '_module_alias', alias)

    def _load_module(self):
        """Load the module and return it.

        Also try to get the module in global namespace.
        """
        module = importlib.import_module(
            self._module_name,
            self._module_package)
        globals()[self._module_alias] = module
        return module

    def __getattr__(self, name):
        """Load the module and simulate attribute access."""
        return getattr(self._load_module(), name)

    def __setattr__(self, name, value):
        """Load the module and simulate attribute access."""
        return setattr(self._load_module(), name, value)

    def __delattr__(self, name):
        """Load the module and simulate attribute access."""
        return delattr(self._load_module(), name)

def lazy_import(name, package=None, alias=None):
    globals()[alias or name] = ModuleProxy(name, package, alias or name)

# C-compiled
import array
import datetime
import itertools
import math
import operator
import os
import sys
import unicodedata

# Imports by name
from pprint import pprint
from functools import reduce
from fractions import Rational, gcd
from decimal import Decimal

# Common
lazy_import("array")
lazy_import("calendar")
lazy_import("collections")
lazy_import("dateutil")
lazy_import("encodings")
lazy_import("md5")
lazy_import("decimal")
lazy_import("fractions")
lazy_import("pickle")
lazy_import("platform")
lazy_import("pyparsing")
lazy_import("re")
lazy_import("time")
lazy_import("timeit")
lazy_import("random")
lazy_import("string")

# Scientific
lazy_import("numpy", alias="np")
lazy_import("scipy", alias="sp")
lazy_import("matplotlib", alias="mpl")
lazy_import("matplotlib.pyplot", alias="plt")
lazy_import("pandas", alias="pd")
lazy_import("sklearn")
lazy_import("scipy.constants", alias="constants")
lazy_import("scipy.fftpack", alias="fftpack")
lazy_import("scipy.integrate", alias="integrate")
lazy_import("scipy.interpolate", alias="interpolate")
lazy_import("scipy.io", alias="io")
lazy_import("scipy.linalg", alias="linalg")
lazy_import("scipy.ndimage", alias="ndimage")
lazy_import("scipy.odr", alias="odr")
lazy_import("scipy.optimize", alias="optimize")
lazy_import("scipy.signal", alias="signal")
lazy_import("scipy.sparse", alias="sparse")
lazy_import("scipy.spatial", alias="spatial")
lazy_import("scipy.special", alias="special")
lazy_import("scipy.stats", alias="stats")
lazy_import("scipy.weave", alias="weave")
lazy_import("networkx")

# flake8: noqa
# vim:set et sw=4 ts=8:
