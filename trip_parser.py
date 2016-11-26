#!/usr/bin/ python
# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser
from tripcalc.lexer import Lexer
from tripcalc.parser import Parser

def main():
  args = buildArgumentParser().parse_args()
  if not args.file:
    print """Please specify a file to parse
    e.g. python trip_parser.py -f filename.txt
    """
    sys.exit(1)

  p = Parser()
  p.parse(Lexer("data.txt").lex())
  print p.output()
  sys.exit(0)

def buildArgumentParser():
  parser = ArgumentParser(description="Vehicle Trip Tracker")
  parser.add_argument('-f', '--file', 
      help="Specify a file to parse",
      type=str)
  return parser

if __name__ == '__main__':
  main()
