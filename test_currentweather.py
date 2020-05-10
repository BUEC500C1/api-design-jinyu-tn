#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:18:41 2020

@author: taimaame
"""

from currentweather import codetoname
from currentweather import print_current_weather
from currentweather import getweather

def test_codetoname():
    assert codetoname('Total Rf Heliport') == 'Bensalem'
    assert codetoname('Slater Field') == 'Federalsburg'
    assert codetoname('Goltl Airport') == 'McDonald'
    assert codetoname('Lazy JAerodrome') == "Wrong"
    assert codetoname('Kellie ManAirfield') == "Wrong"


def test_print_current_weather():
	pass


def test_getweather():
	assert getweather("Kitchen Creek Helibase Heliport") == True
	assert getweather("Lt World Airport") == True
	assert getweather("R J Heliport") == False
	assert getweather("Bailey Genation Station Heliport") == False
