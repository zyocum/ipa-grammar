#!/usr/bin/env python3

import sys
from contextlib import closing
from lark import Lark
from lark import tree
from pathlib import Path
from unicodedata import normalize

def load_grammar(filename):
    with open(filename, mode='r') as f:
        return Lark(f.read(), start='transcription')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__
    )
    parser.add_argument(
        'input',
        type=argparse.FileType('r'),
        help='path to file to read input from (use "-" to read from stdin)'
    )
    parser.add_argument(
        '-o', '--output',
        default=None,
        type=Path,
        help='path to file where graphviz graph will be written',
    )
    parser.add_argument(
        '-g', '--grammar',
        default='ipa.lark',
        type=Path,
        help='path to .lark grammar file',
    )
    args = parser.parse_args()
    parser = load_grammar(args.grammar)
    with closing(args.input) as f:
        sentence = normalize('NFD', f.read())
        try:
            print(parser.parse(sentence).pretty())
            if args.output:
                tree.pydot__tree_to_dot(parser.parse(sentence), args.output)
        except Exception as e:
            print(e, file=sys.stderr)
            sys.exit(1)