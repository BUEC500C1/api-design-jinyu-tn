#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:18:41 2020

@author: taimaame
"""

from currentweather import codetoname

def test_codetoname():
    assert codetoname('Total Rf Heliport') == 'Bensalem'
    assert codetoname('Slater Field') == 'Federalsburg'
    assert codetoname('Goltl Airport') == 'McDonald'
    assert codetoname('Lazy J. Aerodrome') == 'Beverly'
    assert codetoname('Kellie Mann Airfield') == 'Ottawa'