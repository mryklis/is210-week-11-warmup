#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""this module works with classes and functions"""


import time


class Snapshot(object):

    '''snapshot of time
    '''

    def __init__(self,):

        ''' function for snapshot class

        Returns:
            created(float): time to evaluate

        Example:
            >>>>>> mysnap = Snapshot()
            >>> hasattr(mysnap, 'created')
            True

        '''

        self.created = time.time()
