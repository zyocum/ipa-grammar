# ipa-grammar

Basic grammar for parsing International Phonetic Alphabet (IPA) transcriptions

## Setup

To graphically visualize parse trees, you'll need to install [Graphviz](https://graphviz.org/) from your package manager of choice.

For example, from [Homebrew](https://brew.sh/) on macOS:

```zsh
$ brew install graphviz
...
```

Install the dependencies in a Python virtual environment:

```zsh
$ python3 -m venv ipa
$ source ipa/bin/activate
(ipa) $ pip3 install -U pip
(ipa) $ pip3 install -r requirements.txt
...
```

To use the virtual environment in the Jupyter notebook, run:

```zsh
(ipa) $ ipython kernel install --user --name=ipa
(ipa) $ jupyter notebook ipa_grammar.py
```

Then, choose the kernel with the name of the virtual environment:

![Select the "ipa" kernal](kernel.png "kernel selection screenshot")

## `ipa_grammar.py`

The `ipa_grammar.py` script has a basic CLI that allows you to read a "sentence" from a file (or `stdin`) and parse it with a given `.lark` grammar.  The script will attempt to pretty-print a parse tree as text and additionally generate a `.gv` graph that can be rendered as an image by Graphviz's `dot` program.

```zsh
(ipa) $ ./ipa_grammar.py -h
usage: ipa_grammar.py [-h] [-o OUTPUT] [-g GRAMMAR] input

positional arguments:
  input                 path to file to read input from (use "-" to read from stdin)

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to file where graphviz graph will be written (default: ipa.gv)
  -g GRAMMAR, --grammar GRAMMAR
                        path to .lark grammar file (default: ipa.lark)
```

For example:

```zsh
(ipa) $ echo '[kʰæt]' > cat-transcription.txt
(ipa) $ ./ipa_grammar.py cat-transcription.txt -g ipa.lark -o cat.gv
transcription
  phonetic
    None
    phonemes
      phoneme
        c
        cfeatures
          cfeature
      phoneme
        v
        None
        None
      phoneme
        c
        None
(ipa) $ dot -Tpng -o cat.png cat.gv
```

This will generate a graphical parse tree in the file `cat.png`:

![Graphical parse tree](cat.png "parse tree of the English transcription of the word cat")
