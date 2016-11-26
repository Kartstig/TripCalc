#!/usr/bin/ python
# -*- coding: utf-8 -*-

import pytest
from tripcalc.lexer import Lexer, FileNotFoundError

def test_lex():
  l = Lexer("tests/test_data/lextest.txt")
  expected = [
    ['Space','Delmited','Tokens','1','1.202'],
    ['Gap','in','Token']
  ]
  for idx, tokens in enumerate(l.lex()):
    assert expected[idx] == tokens

def test_io_err():
  with pytest.raises(FileNotFoundError) as excinfo:
    l = Lexer("file_does_not_exist")
    print excinfo.value
  assert "File does not exist" == str(excinfo.value)
