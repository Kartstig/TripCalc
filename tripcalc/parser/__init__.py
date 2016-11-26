#!/usr/bin/ python
# -*- coding: utf-8 -*-

import sys

from tripcalc.models.Driver import Driver

class Parser():
  TIME_FMT = "%H:%M"
  TOKENS = {
    "Driver": "t_driver",
    "Trip": "t_trip"
  }

  def __init__(self):
    self.drivers = dict()

  def parse(self, token_generator):
    for tokens in token_generator:
      tok = self.TOKENS.get(tokens[0], None)
      if tok:
        func = getattr(self, tok)
        func(tokens)
      else:
        raise ParseError("Unexpected Token: {}".format(tokens[0]))

  def t_driver(self, args):
    if len(args) != 2:
      raise ParseError("Incorrect number of arguments for: {}".format(args[0]))
    driver = str(args[1])
    if not driver in self.drivers:
      self.drivers[driver] = Driver(driver)

  def t_trip(self, args):
    if len(args) != 5:
      raise ParseError("Incorrect number of arguments for: {}".format(args[0]))
    driver = str(args[1])
    if driver not in self.drivers:
      raise ParseError("Uninitialized driver: {}".format(driver))
    self.drivers[driver].drive(*args[2:])

  def output(self):
    output = ""
    drivers = [self.drivers[d] for d in self.drivers]
    res = sorted(drivers, key=lambda d: d.miles, reverse=True)
    for driver in res:
      output += str(driver)
    return output
    
class ParseError(Exception):
  pass
