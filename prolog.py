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
        r"Are "+word_pattern+r" and "+word_pattern+r" siblings?",
        r"Is "+word_pattern+r" a "+word_pattern+r" of "+word_pattern+r"\?",
        r"Is "+word_pattern+r" an [(uncle)|(aunt)] of "+word_pattern+r"\?",
        r"Are "+word_pattern+r" and "+word_pattern+r" the parent of "+word_pattern+r"\?",
        r"Are "+word_pattern+r", "+word_pattern+r" and "+word_pattern+r" children of "+word_pattern+r"\?",
        r"Who are the "+word_pattern+r" of "+word_pattern+r"\?",
        r"Who is the "+word_pattern+r" of "+word_pattern+r"\?",
        r"Are "+word_pattern+r" and "+word_pattern+r" relatives\?"




    ]