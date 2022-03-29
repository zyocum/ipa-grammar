#!/usr/bin/env python3

from pathlib import Path
from contextlib import closing
from lark import Lark
from lark import tree

def load_grammar(filename='ipa.lark'):
    with open(filename, mode='r') as f:
        return Lark(f.read(), start='transcription')

def make_dot(sentence, parser, filename='ipa.gv'):
    tree.pydot__tree_to_dot(parser.parse(sentence), filename)

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
        default='ipa.gv',
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
        sentence = f.read()
        try:
            print(parser.parse(sentence).pretty())
            make_dot(sentence, parser, filename=args.output)
        except Exception as e:
            print(e)
