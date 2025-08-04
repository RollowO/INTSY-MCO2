import re
from pyswip import Prolog
import os

def init_prolog():
    prolog = Prolog()
    prolog.consult("Relations.pl")
    return prolog

def parse():
    word_pattern = r"(^\b\w+\b$)"
    fact_patterns = [
        word_pattern+r" is a (\b\w+\b) of "+word_pattern,
        word_pattern+r" is the "+word_pattern+r" of "+word_pattern,
        word_pattern+r" is an "+word_pattern+r" of "+word_pattern,
        word_pattern+r" and "+word_pattern+r" are siblings",
        word_pattern+r", "+word_pattern+r" and "+word_pattern+r" are children of "+word_pattern
    ]

    query_patterns=[

    ]