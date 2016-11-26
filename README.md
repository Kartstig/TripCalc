# TripCalc

My general approach to solving this problem was to split it up into 3 segments:

1. A [Lexer](https://github.com/Kartstig/TripCalc/blob/master/tripcalc/lexer/__init__.py) to provide a means of tokenizing the inputs
2. A [Parser](https://github.com/Kartstig/TripCalc/blob/master/tripcalc/parser/__init__.py) to provide a means of evaluating tokens
3. A [Driver](https://github.com/Kartstig/TripCalc/blob/master/tripcalc/models/Driver.py) model to handle state transactions and output formatting

I started testing in the order of execution. First, I wrote some tests to ensure the Lexer is [handling the input properly](https://github.com/Kartstig/TripCalc/blob/master/tests/lexer_test.py#L14), AND that it [deals with errors](https://github.com/Kartstig/TripCalc/blob/master/tests/lexer_test.py#L20) when it encounters them. Next I wrote some tests for the parser. Since the Parser implements the Driver model, and I wrote some extensive tests for it, I ended up just stopping there. I think that there should be tests for the Driver model specifically (e.g. avg_mph), but it's arguable that it's being tested by the [output function](https://github.com/Kartstig/TripCalc/blob/master/tests/parser_test.py#L67), and so I felt it was fine to stop there. Plus, code coverage is 99%...

Please feel free to [email me](mailto: kartstig@gmail.com) me know if you have any questions. Thanks!

## Setup
Run the following
```bash
$ script/setup
```
## Usage
```bash
$ venv/bin/python trip_parser.py -f filename.txt
```
## Tests
To run all tests
```bash
$ script/test
```
