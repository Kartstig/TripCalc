#!/usr/bin/ python
# -*- coding: utf-8 -*-

import os

class Lexer():

  def __init__(self, filename):
    if not os.path.isfile(filename):
      raise FileNotFoundError("File does not exist")
    self.filename = filename

  def lex(self):
    for line in self.parse_lines():
      yield line.split()

  def parse_lines(self):
    with open(self.filename, 'r') as f:
      for line in f:
        if not line == "\n":
          yield line

class FileNotFoundError(IOError):
  pass
