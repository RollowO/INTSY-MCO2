import re
from pyswip import Prolog
import os

def todo():
    return "Nothing"
def init_prolog():
    prolog = Prolog()
    prolog.consult("Relations.pl")
    return prolog

def get_family_type(match):
    return match.group(1)


def parse(user_input):
    # thank you stalgcm for teaching me regex - renzo
    family_types_one = r"(sister|brother|grandmother|grandfather|child|daughter|son)"
    family_types_two = r"(mother|father)"
    family_types_three = r"(uncle|aunt)"
    family_types_four=r"(sisters|brothers|parents|daughters|sons|siblings|children)"
    word_pattern = r"(\b\w+\b)"
    fact_patterns = [
        word_pattern+r" is a "+family_types_one+r" of "+word_pattern,
        word_pattern+r" is the (mother|father) of "+word_pattern,
        word_pattern+r" is an (uncle|aunt) of "+word_pattern,
        word_pattern+r" and "+word_pattern+r" are siblings",
        word_pattern+r", "+word_pattern+r" and "+word_pattern+r" are children of "+word_pattern
    ]

    query_patterns=[
        r"Are "+word_pattern+r" and "+word_pattern+r" siblings\?",
        r"Is "+word_pattern+r" a "+family_types_one+r" of "+word_pattern+r"\?",
        r"Is "+word_pattern+r" an "+family_types_three+r" of "+word_pattern+r"\?",
        r"Are "+word_pattern+r" and "+word_pattern+r" the parents of "+word_pattern+r"\?",
        r"Are "+word_pattern+r", "+word_pattern+r" and "+word_pattern+r" children of "+word_pattern+r"\?",
        r"Who are the "+family_types_four+r" of "+word_pattern+r"\?",
        r"Who is the "+family_types_two+r" of "+word_pattern+r"\?",
        r"Are "+word_pattern+r" and "+word_pattern+r" relatives\?"

    ]

    for index,pattern in enumerate(fact_patterns):
        match = re.fullmatch(pattern,user_input)
        if(match):
            print("MATCHED")
            print(get_family_type(match))
            if(index == 0):
                family_type = get_family_type(match)
                todo()
            elif(index == 1):
                family_type = get_family_type(match)
                todo()
            elif(index == 2):
                family_type = get_family_type(match)
                todo()
            elif(index == 3):
                todo()
            elif(index == 4):
                todo()
                
    for index,pattern in enumerate(query_patterns):
        match = re.fullmatch(pattern,user_input)
        if(match):
            print("MATCHED QUERY")
            print(match.groups())
            if(index == 0):
                todo()
            elif(index == 1):
                todo()
            elif(index == 2):
                todo()
            elif(index == 3):
                todo()
            elif(index == 4):
                todo()
            elif(index == 5):
                todo()
            elif(index == 6):
                todo()
            elif(index == 7):
                todo()




def __main__():
    while True:
        user_input = input("Prompt something about family relationships")
        if(user_input == "exit"):
            break
        else:
            parse(user_input)

__main__()