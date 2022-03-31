#!/usr/bin/env zsh
TESTDEFAULT=${0:a:h}/test-transcriptions.txt
TESTFILE=${1:=$TESTDEFAULT}

time ( \
  while read l; do
    echo -n "$l " \
      | tee /dev/stderr \
      | (./ipa_grammar.py - >/dev/null 2>/dev/null) \
    && echo 'PASS' || echo 'FAIL'
  done < $TESTFILE
)