import re
from pyswip import Prolog

prolog = Prolog()

def handle_father(match):
    father, child = match.groups()
    try:
        female = list(prolog.query(f"female({father})"))
        # Check if child already has a father
        has_father = list(prolog.query(f"father(X, {child})"))
        # Prevent father from being the grandmother of the child
        is_grandmother = list(prolog.query(f"grandmother({father}, {child})"))
    except Exception:
        female = False
        has_father = False
        is_grandmother = False
    if female:
        print(f"That's impossible!")
        return
    if has_father and len(has_father) >= 1:
        print(f"That's impossible! {child} already has a father.")
        return
    if is_grandmother:
        print(f"That's impossible! A grandmother can't also be the father of her grandchild.")
        return
    prolog.assertz(f"father({father}, {child})")
    prolog.assertz(f"male({father})") #When one becomes a father, male is asserted
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
    prolog.assertz(f"female({sister})") #When one becomes a sister, female is asserted
    print(f"Added: sister({sister}, {sibling})")

def handle_mother(match):
    mother, child = match.groups()
    try:
        Male = list(prolog.query(f"male({mother})")) #mother cannot be a male
        # Check if child already has a mother
        has_mother = list(prolog.query(f"mother(X, {child})"))
        # Prevent mother from being the grandmother of the child
        is_grandmother = list(prolog.query(f"grandmother({mother}, {child})"))
    except Exception:
        Male = False
        has_mother = False
        is_grandmother = False
    if Male:
        print(f"That's impossible!")
        return
    if has_mother:
        print(f"That's impossible! {child} already has a mother.")
        return
    if is_grandmother:
        print(f"That's impossible! A grandmother can't also be the mother of her grandchild.")
        return
    prolog.assertz(f"mother({mother}, {child})")
    prolog.assertz(f"female({mother})") #When one becomes a mother, female is asserted
    print(f"Added: mother({mother}, {child}) and female({mother})")

def handle_grandmother(match):
    grandmother, grandchild = match.groups()
    try:
        Male = list(prolog.query(f"male({grandmother})"))
        # Prevent circular relationship: grandmother cannot be child of grandchild's father
        circular = list(prolog.query(f"father(X, {grandchild})")) and \
                   list(prolog.query(f"child({grandmother}, X)"))
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
                   list(prolog.query(f"father({child}, {parent})")) or \
                   list(prolog.query(f"mother({child}, {parent})")) #father and mother are also considered parents, cannot be child of child
    except Exception:
        circular = False
    if circular:
        print(f"That's impossible!")
        return
    prolog.assertz(f"child({child}, {parent})")
    print(f"Added: child({child}, {parent})")

patterns = [
    (r"(\w+)\s+is the father of\s+(\w+)", handle_father),
    (r"(\w+)\s+and\s+(\w+)\s+are siblings", handle_siblings),
    (r"(\w+)\s+is the sister of\s+(\w+)", handle_sister),
    (r"(\w+)\s+is the mother of\s+(\w+)", handle_mother),
    (r"(\w+)\s+is the grandmother of\s+(\w+)", handle_grandmother),
    (r"(\w+)\s+is the child of\s+(\w+)", handle_child),
]

query_patterns = [
    (r"are (\w+) and (\w+) siblings\?", lambda m: f"sibling({m.group(1)}, {m.group(2)})"),
    (r"is (\w+) a sister of (\w+)\?", lambda m: f"sister({m.group(1)}, {m.group(2)})"),
    (r"Are (\w+)\s+and (\w+)\s+the parents of\s+(\w+)", lambda m: f"father({m.group(1)}, {m.group(3)})"),
    (r"Is (\w+)\s+the mother of\s+(\w+)\?", lambda m: f"mother({m.group(1)}, {m.group(2)})"),
    (r"Is (\w+)\s+the father of\s+(\w+)\?", lambda m: f"father({m.group(1)}, {m.group(2)})"),
    (r"Is (\w+)\s+the grandmother of\s+(\w+)\?", lambda m: f"grandmother({m.group(1)}, {m.group(2)})"),
    (r"Is (\w+)\s+the child of\s+(\w+)\?", lambda m: f"child({m.group(1)}, {m.group(2)})"),
]

def main():
    print("Enter relationships or queries (type 'exit' to stop):")
    while True:
        statement = input(">> ").strip().lower()
        if statement == "exit":
            break

        # Check for sentence-based queries first
        for pattern, query_builder in query_patterns:
            match = re.match(pattern, statement)
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
            # Fallback to direct Prolog queries with '?'
            if "?" in statement:
                query = statement.replace("?", "").strip()
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

            # Relationship statements
            for pattern, handler in patterns:
                match = re.match(pattern, statement)
                if match:
                    handler(match)
                    break
            else:
                print("Please follow a sentence pattern.")

if __name__ == "__main__":
    main()