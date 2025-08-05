import re
from pyswip import Prolog
from facts import Facts
from query import Query
import os

def todo():
    return "Nothing"
def init_prolog():
    prolog = Prolog()
    prolog.consult("./Relations.pl")
    return prolog

def get_family_type(match):
    return match.group(2)


def parse(user_input,prolog):
    # thank you stalgcm for teaching me regex - renzo
    family_types_one = r"(sister|brother|grandmother|grandfather|child|daughter|son)"
    family_types_two = r"(mother|father)"
    family_types_three = r"(uncle|aunt)"
    family_types_four=r"(sisters|brothers|parents|daughters|sons|siblings|children)"
    word_pattern = r"(\b\w+\b)"
    fact_patterns = [
        word_pattern+r" is a "+family_types_one+r" of "+word_pattern,
        word_pattern+r" is the "+family_types_two+r" of "+word_pattern,
        word_pattern+r" is an "+family_types_three+r" of "+word_pattern,
        word_pattern+r" and "+word_pattern+r" are siblings",
        word_pattern+r", "+word_pattern+r" and "+word_pattern+r" are children of "+word_pattern,
        word_pattern+r" and "+word_pattern+r" are the parents of "+word_pattern
    ]

    query_patterns=[
        r"Are "+word_pattern+r" and "+word_pattern+r" siblings\?", 
        r"Is "+word_pattern+r" a "+family_types_one+r" of "+word_pattern+r"\?",
        r"Is "+word_pattern+r" an "+family_types_three+r" of "+word_pattern+r"\?",
        r"Is "+word_pattern+r" the "+family_types_two+r" of "+word_pattern+r"\?",
        r"Are "+word_pattern+r" and "+word_pattern+r" the parents of "+word_pattern+r"\?",
        r"Are "+word_pattern+r", "+word_pattern+r" and "+word_pattern+r" children of "+word_pattern+r"\?",
        r"Who are the "+family_types_four+r" of "+word_pattern+r"\?",
        r"Who is the "+family_types_two+r" of "+word_pattern+r"\?",
        r"Are "+word_pattern+r" and "+word_pattern+r" relatives\?"

    ]

    for index,pattern in enumerate(fact_patterns):
        match = re.fullmatch(pattern,user_input)
        if(match):
            print("match!")
            if(index == 0):
                family_type = get_family_type(match)
                Facts.execute_typeof_family(family_type,match.group(1),match.group(3),prolog)

            elif(index == 1):
                family_type = get_family_type(match)
                Facts.execute_typeof_family(family_type,match.group(1),match.group(3),prolog)
            elif(index == 2):
                family_type = get_family_type(match)
                Facts.execute_typeof_family(family_type,match.group(1),match.group(3),prolog)
            elif(index == 3):
                name_one = match.group(1)
                name_two = match.group(2)
                Facts.siblings(prolog,name_one,name_two)
                todo()
            elif(index == 4):
                name_one = match.group(1)
                name_two = match.group(2)
                name_three = match.group(3)
                name_four = match.group(4)
                Facts.children(prolog,name_one,name_two,name_three,name_four)
                todo()
            elif(index == 5):
                name_one = match.group(1)
                name_two = match.group(2)
                name_three = match.group(3)
                Facts.parents(prolog,name_one,name_two,name_three)
                
    for index,pattern in enumerate(query_patterns):
        match = re.fullmatch(pattern,user_input)
        if(match):
            print(match.groups())
            if(index == 0):
                # Are __ and __ siblings
                name_one = match.group(1)
                name_two = match.group(2)
                Query.query_siblings(p=prolog,x=name_one,y=name_two)
            elif(index == 1):
                # 1- 3 == Is _ a/an/the __ of __
                family_type = get_family_type(match)
                name_one = match.group(1)
                name_two = match.group(3)
                Query.execute_is_x_typeof_y(family_type,x=name_one,y=name_two,p=prolog)
                todo()
            elif(index == 2):
                family_type = get_family_type(match)
                name_one = match.group(1)
                name_two = match.group(3)
                Query.execute_is_x_typeof_y(family_type,x=name_one,y=name_two,p=prolog)
                todo()
            elif(index == 3):
                family_type = get_family_type(match)
                name_one = match.group(1)
                name_two = match.group(3)
                Query.execute_is_x_typeof_y(family_type,x=name_one,y=name_two,p=prolog)
                todo()
            elif(index == 4):
                # Are _ and _ the parents of _
                name_one = match.group(1)
                name_two = match.group(2)
                name_three = match.group(3)                    
                Query.query_parents(x=name_one,y=name_two,z=name_three,p=prolog)
                todo()
            elif(index == 5):
                # Are _ _ _ children of _
                name_one = match.group(1)
                name_two = match.group(2)
                name_three = match.group(3)
                name_four = match.group(4)
                Query.query_children(x=name_one,y=name_two,z=name_three,a=name_four,p=prolog)
                todo()
            elif(index == 6):
                # Who are the __ of __
                family_type = match.group(1)
                name_one = match.group(2)
                Query.execute_relations_of_x(typeof=family_type,x=name_one,p=prolog)
            elif(index == 7):
                # Who is the __ of __
                family_type = match.group(1)
                name_one = match.group(2)
                Query.execute_relations_of_x(typeof=family_type,x=name_one,p=prolog)


            elif(index == 8):
                # Are _ and _ relatives?
                name_one = match.group(1)
                name_two = match.group(2)
                Query.query_relatives(p=prolog,x=name_one,y=name_two)
                todo()




def __main__():
    prolog = init_prolog()
    while True:
        user_input = input("Prompt something about family relationships - ")
        if(user_input == "exit"):
            break
        else:
            parse(user_input, prolog)

__main__()