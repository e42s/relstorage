##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
IOIDAllocator implementations.
"""

from __future__ import absolute_import

import six
import abc

@six.add_metaclass(abc.ABCMeta)
class AbstractOIDAllocator(object):

    @abc.abstractmethod
    def set_min_oid(self, cursor, oid):
        raise NotImplementedError()

    @abc.abstractmethod
    def new_oids(self, cursor):
        raise NotImplementedError()

    # All of these allocators allocate 16 OIDs at a time.  In the sequence
    # or table, value (n) represents (n * 16 - 15) through (n * 16).  So,
    # value 1 represents OID block 1-16, 2 represents OID block 17-32,
    # and so on. The _oid_range_around helper method returns a list
    # around this number sorted in the proper way.
    # Note than range(n * 16 - 15, n*16+1).sort(reverse=True)
    # is the same as range(n * 16, n*16 -16, -1)
    if isinstance(range(1), list):
        # Py2
        def _oid_range_around(self, n):
            return range(n * 16, n * 16 - 16, -1)
    else:
        def _oid_range_around(self, n):
            l = list(range(n * 16, n * 16 - 16, -1))
            l.sort(reverse=True)
            return l
