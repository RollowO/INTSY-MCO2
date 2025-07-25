import re
from pyswip import Prolog

prolog = Prolog()
prolog.consult("Relations.pl")

def handle_father(match):
    father, child = match.groups()
    try:
        female = list(prolog.query(f"female({father})"))
    except Exception:
        female = False
    if female:
        print(f"That's impossible!")
        return
   
    prolog.assertz(f"father({father}, {child})")
    prolog.assertz(f"male({father})")
    print(f"Added: father({father}, {child}) and male({father})")

def handle_siblings(match):
    a, b = match.groups()
    prolog.assertz(f"sibling({a}, {b})")
    prolog.assertz(f"sibling({b}, {a})")
    print(f"Added: sibling({a}, {b}) and sibling({b}, {a})")

def handle_sister(match):
    sister, sibling = match.groups()
    try:
        Male = list(prolog.query(f"male({sister})"))
    except Exception:
        Male = False
    if Male:
        print(f"That's impossible!")
        return
    prolog.assertz(f"sister({sister}, {sibling})")
    prolog.assertz(f"female({sister})")
    print(f"Added: sister({sister}, {sibling}) and female({sister})")

def handle_mother(match):
    mother, child = match.groups()
    try:
        # Check if already declared male
        is_male = list(prolog.query(f"male({mother})"))
    except Exception:
        is_male = False

    if is_male:
        print(f"That's impossible! {mother} is male and cannot be a mother.")
        return

    try:
        has_mother = list(prolog.query(f"mother(X, {child})"))
        is_grandmother = list(prolog.query(f"grandmother({mother}, {child})"))
    except Exception:
        has_mother = False
        is_grandmother = False

    if has_mother:
        print(f"That's impossible! {child} already has a mother.")
        return
    if is_grandmother:
        print(f"That's impossible! A grandmother can't also be the mother of her grandchild.")
        return

    prolog.assertz(f"mother({mother}, {child})")
    prolog.assertz(f"female({mother})")
    print(f"Added: mother({mother}, {child}) and female({mother})")


def handle_grandmother(match):
    grandmother, grandchild = match.groups()
    try:
        Male = list(prolog.query(f"male({grandmother})"))
        # Prevent circular relationship: grandchild cannot be the grandmother of a grandmother
        circular = list(prolog.query(f"grandparent({grandchild}, {grandmother})"))
        # Prevent grandmother from being the mother or father of the grandchild
        is_mother = list(prolog.query(f"mother({grandmother}, {grandchild})"))
        is_father = list(prolog.query(f"father({grandmother}, {grandchild})"))
        # Prevent child's mother or father from being the grandmother
        parent_is_grandmother = list(prolog.query(f"mother(X, {grandchild}), grandmother({grandmother}, {grandchild}), X={grandmother}")) or \
                                list(prolog.query(f"father(X, {grandchild}), grandmother({grandmother}, {grandchild}), X={grandmother}"))
    except Exception:
        Male = False
        circular = False
        is_mother = False
        is_father = False
        parent_is_grandmother = False
    if Male:
        print(f"That's impossible!")
        return
    if circular:
        print(f"That's impossible! A child can't be the grandmother of a father.")
        return
    if is_mother or is_father:
        print(f"That's impossible! A grandmother can't be the mother or father of her grandchild.")
        return
    if parent_is_grandmother:
        print(f"That's impossible! A child's mother or father can't also be their grandmother.")
        return
    prolog.assertz(f"grandmother({grandmother}, {grandchild})")
    prolog.assertz(f"female({grandmother})")
    print(f"Added: grandmother({grandmother}, {grandchild}) and female({grandmother})")

def handle_child(match):
    child, parent = match.groups()
    try:
        circular = list(prolog.query(f"child({parent}, {child})")) or \
                   list(prolog.query(f"parent({child}, {parent})")) #parents cannot be children of their own child
    except Exception:
        circular = False
    if circular:
        print(f"That's impossible!")
        return
    prolog.assertz(f"child({child}, {parent})")
    print(f"Added: child({child}, {parent})")

def handle_daughter(match):
    daughter, parent = match.groups()   
    try:
        circular = list(prolog.query(f"child({parent}, {daughter})")) or \
                   list(prolog.query(f"parent({daughter}, {parent})")) 
    except Exception:
        circular = False
    if circular:
        print(f"That's impossible!")
        return
    prolog.assertz(f"daughter({daughter}, {parent})")
    print(f"Added: daughter({daughter}, {parent})")

def handle_uncle(match):
    uncle, nephew = match.groups()
    try:
        Male = list(prolog.query(f"male({uncle})"))
        # Prevent circular relationship: uncle cannot be nephew of uncle
        circular = list(prolog.query(f"uncle({nephew}, {uncle})"))
        # Prevent child's mother or father from being the uncle
        parent_is_uncle = list(prolog.query(f"parent({uncle}, {nephew})"))
    except Exception:
        Male = False
        circular = False
        parent_is_uncle = False
    if Male:
        print(f"That's impossible!")
        return
    if circular:
        print(f"That's impossible! A child can't be the uncle of a father.")
        return
    if parent_is_uncle:
        print(f"That's impossible! A child's mother or father can't also be their uncle.")
        return
    prolog.assertz(f"uncle({uncle}, {nephew})")
    print(f"Added: uncle({uncle}, {nephew})")

def handle_brother(match):
    brother, sibling = match.groups()
    try:
        circular = list(prolog.query(f"child({brother}, {sibling})")) and \
                   list(prolog.query(f"child({sibling}, {brother})"))
    except Exception:
        circular = False
    if circular:
        print(f"That's impossible! A brother can't be a sibling of himself.")
        return
    prolog.assertz(f"brother({brother}, {sibling})")
    prolog.assertz(f"male({brother})")
    print(f"Added: brother({brother}, {sibling}) and male({brother})")

def handle_parents(match):
    parent1, parent2, child = match.groups()
    try:
        circular = list(prolog.query(f"parent({child}, {parent1})")) or \
                   list(prolog.query(f"parent({child}, {parent2})"))
    except Exception:
        circular = False
    if circular:
        print(f"That's impossible! A parent can't be a child of their own child.")
        return
    prolog.assertz(f"parent({parent1}, {child})")
    prolog.assertz(f"parent({parent2}, {child})")
    print(f"Added: parent({parent1}, {child}) and parent({parent2}, {child})")

def handle_grandfather(match):
    grandfather, grandchild = match.groups()
    try:
        circular = list(prolog.query(f"grandfather({grandchild}, {grandfather})")) and \
                   list(prolog.query(f"female({grandfather})")) # grandfather cannot be female
    except Exception:
        circular = False
    if circular:
        print(f"That's impossible! A grandfather can't be a grandchild of himself.")
        return
    prolog.assertz(f"grandfather({grandfather}, {grandchild})")
    prolog.assertz(f"male({grandfather})")
    print(f"Added: grandfather({grandfather}, {grandchild}) and male({grandfather})")


def handle_children(match):
    children = match.groups()
    parent = children[-1]
    for child in children[:-1]:
        try:
            circular = list(prolog.query(f"child({parent}, {child})")) or \
                        list(prolog.query(f"father({child}, {parent})"))
        except Exception:
            circular = False
        if circular:
            print(f"That's impossible! A parent can't be a child of their own child.")
            return
        prolog.assertz(f"child({child}, {parent})")

def handle_son(match):
    son, parent = match.groups()
    try:
        circular = list(prolog.query(f"child({parent}, {son})")) or \
                   list(prolog.query(f"father({son}, {parent})")) or \
                   list(prolog.query(f"mother({son}, {parent})")) #father and mother are also considered parents, cannot be child of child
    except Exception:
        circular = False
    if circular:
        print(f"That's impossible! A parent can't be a child of their own child.")
        return
    prolog.assertz(f"son({son}, {parent})")
    prolog.assertz(f"male({son})")
    print(f"Added: son({son}, {parent}) and male({son})")

def handle_aunt(match): ####################BUGS FOR RELATIONS IN RELATIONS.PL, NEED TO CHANGE ASSERTZ TO FOLLOW RULES###############################
    aunt, niece = match.groups()
    try:
        circular = list(prolog.query(f"aunt({aunt}, {aunt})"))
    except Exception:
        circular = False
    if circular:
        print(f"That's impossible! An aunt can't be a niece of herself.")
        return
    prolog.assertz(f"aunt({aunt}, {niece})")
    print(f"Added: aunt({aunt}, {niece})")


patterns = [
    (r"(\w+)\s+is the father of\s+(\w+)\.?", handle_father),
    (r"(\w+)\s+and\s+(\w+)\s+are siblings\.?", handle_siblings),
    (r"(\w+)\s+is the sister of\s+(\w+)\.?", handle_sister),
    (r"(\w+)\s+is the mother of\s+(\w+)\.?", handle_mother),
    (r"(\w+)\s+is the grandmother of\s+(\w+)\.?", handle_grandmother),
    (r"(\w+)\s+is the child of\s+(\w+)\.?", handle_child),
    (r"(\w+)\s+is the daughter of\s+(\w+)\.?", handle_daughter),
    (r"(\w+)\s+is the uncle of\s+(\w+)\.?", handle_uncle),
    (r"(\w+)\s+is the brother of\s+(\w+)\.?", handle_brother),
    (r"(\w+)\s+and\s+(\w+)\s+are the parents of\s+(\w+)\.?", handle_parents),
    (r"(\w+)\s+is the grandfather of\s+(\w+)\.?", handle_grandfather),
    (r"(\w+)\s+and\s+(\w+)\s+and\s+(\w+)\s+are the children of\s+(\w+)\.?", handle_children),
    (r"(\w+)\s+is the son of\s+(\w+)\.?", handle_son),
    (r"(\w+)\s+is the aunt of\s+(\w+)\.?", handle_aunt),
]

query_patterns = [
    (r"Are (\w+) and (\w+) siblings\?", lambda m: f"sibling({m.group(1)}, {m.group(2)})"),
    (r"Who are the siblings of (\w+)\?", lambda m: f"sibling(X, {m.group(1)})"),
    
    (r"Is (\w+) a sister of (\w+)\?", lambda m: f"sister({m.group(1)}, {m.group(2)})"),
    (r"Who are the sisters of (\w+)\?", lambda m: f"sister(X, {m.group(1)})"),
    
    (r"Is (\w+) a brother of (\w+)\?", lambda m: f"brother({m.group(1)}, {m.group(2)})"),
    (r"Who are the brothers of (\w+)\?", lambda m: f"brother(X, {m.group(1)})"),

    (r"Is (\w+) the mother of (\w+)\?", lambda m: f"mother({m.group(1)}, {m.group(2)})"),
    (r"Who is the mother of (\w+)\?", lambda m: f"mother(X, {m.group(1)})"),

    (r"Is (\w+) the father of (\w+)\?", lambda m: f"father({m.group(1)}, {m.group(2)})"),
    (r"Who is the father of (\w+)\?", lambda m: f"father(X, {m.group(1)})"),

    (r"Are (\w+) and (\w+) the parents of (\w+)\?", lambda m: f"parent({m.group(1)}, {m.group(3)}) , parent({m.group(2)}, {m.group(3)})"),
    (r"Who are the parents of (\w+)\?", lambda m: f"parent(X, {m.group(1)})"),

    (r"Is (\w+) a grandmother of (\w+)\?", lambda m: f"grandmother({m.group(1)}, {m.group(2)})"),
    (r"Is (\w+) a grandfather of (\w+)\?", lambda m: f"grandfather({m.group(1)}, {m.group(2)})"),

    (r"Is (\w+) a daughter of (\w+)\?", lambda m: f"daughter({m.group(1)}, {m.group(2)})"),
    (r"Who are the daughters of (\w+)\?", lambda m: f"daughter(X, {m.group(1)})"),

    (r"Is (\w+) a son of (\w+)\?", lambda m: f"son({m.group(1)}, {m.group(2)})"),
    (r"Who are the sons of (\w+)\?", lambda m: f"son(X, {m.group(1)})"),

    (r"Is (\w+) a child of (\w+)\?", lambda m: f"child({m.group(1)}, {m.group(2)})"),
    (r"Who are the children of (\w+)\?", lambda m: f"child(X, {m.group(1)})"),

    (r"Are (\w+), (\w+), and (\w+) children of (\w+)\?", lambda m: f"child({m.group(1)}, {m.group(4)}) , child({m.group(2)}, {m.group(4)}) , child({m.group(3)}, {m.group(4)})"),

    (r"Is (\w+) an uncle of (\w+)\?", lambda m: f"uncle({m.group(1)}, {m.group(2)})"),
    (r"Is (\w+) an aunt of (\w+)\?", lambda m: f"aunt({m.group(1)}, {m.group(2)})"),

    (r"Are (\w+) and (\w+) relatives\?", lambda m: f"relatives({m.group(1)}, {m.group(2)})"),
]


def main():
    print("Enter relationships or queries (type 'exit' to stop):")
    while True:
        statement = input(">> ").strip()
        if statement.lower() == "exit":
            break

        # Normalize trailing punctuation (like '.') and lowercase only for matching, not values
        normalized = statement.rstrip(".? ").strip()

        # Check for sentence-based queries
        for pattern, query_builder in query_patterns:
            match = re.match(pattern, statement, re.IGNORECASE)
            if match:
                query = query_builder(match)
                try:
                    results = list(prolog.query(query))
                    if results:
                        print("Yes.")
                    else:
                        print("No.")
                except Exception as e:
                    print(f"Invalid query: {e}")
                break
        else:
            # Direct Prolog query fallback
            if "?" in statement:
                query = normalized
                try:
                    results = list(prolog.query(query))
                    if results:
                        for result in results:
                            print(result)
                    else:
                        print("No results found.")
                except Exception as e:
                    print(f"Invalid query: {e}")
                continue

            # Relationship sentence matching
            for pattern, handler in patterns:
                match = re.match(pattern, normalized, re.IGNORECASE)
                if match:
                    handler(match)
                    break
            else:
                print("Please follow a sentence pattern.")


if __name__ == "__main__":
    main()