#!/usr/bin/ python
# -*- coding: utf-8 -*-

import pytest
from tripcalc.parser import Parser, ParseError

def test_driver_token_result():
  driver = 'TestDriver1'
  p = Parser()
  p.parse([['Driver', driver]])
  assert driver in p.drivers

def test_trip_token_result():
  driver = 'TestDriver1'
  p = Parser()
  p.parse([['Driver', driver]])
  p.parse([['Trip', driver, '12:00', '12:30', '30.0']])
  assert p.drivers[driver].trips == 1
  assert p.drivers[driver].miles == 30.0
  assert p.drivers[driver].hours == 0.5
  p.parse([['Trip', driver, '12:00', '13:00', '5.0']])
  assert p.drivers[driver].trips == 1
  assert p.drivers[driver].miles == 30.0
  assert p.drivers[driver].hours == 0.5
  p.parse([['Trip', driver, '12:00', '13:00', '6.0']])
  assert p.drivers[driver].trips == 2
  assert p.drivers[driver].miles == 36.0
  assert p.drivers[driver].hours == 1.5

def test_driver_too_many_args():
  p = Parser()
  with pytest.raises(ParseError) as excinfo:
    p.parse([['Driver','this','is','way','too','many','args']])
  assert "Incorrect number of arguments for: Driver" == str(excinfo.value)

def test_driver_too_few_args():
  p = Parser()
  with pytest.raises(ParseError) as excinfo:
    p.parse([['Driver']])
  assert "Incorrect number of arguments for: Driver" == str(excinfo.value)

def test_trip_too_many_args():
  p = Parser()
  with pytest.raises(ParseError) as excinfo:
    p.parse([['Trip','Driver','1','2','3','4']])
  assert "Incorrect number of arguments for: Trip" == str(excinfo.value)

def test_trip_too_few_args():
  p = Parser()
  with pytest.raises(ParseError) as excinfo:
    p.parse([['Trip','Driver']])
  assert "Incorrect number of arguments for: Trip" == str(excinfo.value)

def test_bad_token():
  p = Parser()
  with pytest.raises(ParseError) as excinfo:
    p.parse([['BADTOKEN', 'Meaningless', 'Args']])
  assert "Unexpected Token: BADTOKEN" == str(excinfo.value)

def test_output():
  p = Parser()
  p.parse([['Driver','Herman']])
  p.parse([['Driver','TestDriver']])
  p.parse([['Trip','Herman','12:00','14:00','120.0']])
  p.parse([['Trip','TestDriver','12:00','13:00','60.0']])
  expected = "Herman: 120 miles @ 60 mph\nTestDriver: 60 miles @ 60 mph\n"
  assert p.output() == expected

def test_omitted_output():
  p = Parser()
  p.parse([['Driver','Herman']])
  p.parse([['Trip','Herman','12:00','14:00','90000.0']])
  expected = "Herman: 0 miles\n"
  assert p.output() == expected
