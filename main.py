import re
from pyswip import Prolog
import os

prolog = Prolog()
prolog.consult("./Relations.pl")

def check_gender_conflict(name, expected_gender):
    opposite = "male" if expected_gender == "female" else "female"
    return list(prolog.query(f"{opposite}('{name}')"))

def safe_assert_parent(parent, child):
    query = f"parent('{parent}', '{child}')"
    if not list(prolog.query(query)):
        prolog.assertz(query)
        print(f"Added: parent({parent}, {child})")
    else:
        print(f"Skipped: parent({parent}, {child}) already exists.")

def handle_father(match):
    father, child = match.groups()

    if father == child:
        print("That's impossible! A person can't be their own parent.")
        return

    if check_gender_conflict(father, expected_gender="male"):
        print(f"That's impossible! {father} is already declared female and cannot be a father.")
        return

    ancestor_result = list(prolog.query(f"ancestor('{child}', '{father}')"))
    parent_result = list(prolog.query(f"parent('{child}', '{father}')"))
    contradiction = bool(ancestor_result) or bool(parent_result) or father == child

    if contradiction:
        print("That's impossible! That would create a contradiction.")
        print("[Debug] ancestor check:", ancestor_result)
        print("[Debug] parent check:", parent_result)
        print("[Debug] equality check:", father == child)
        return

    prolog.assertz(f"parent('{father}', '{child}')")
    prolog.assertz(f"male('{father}')")
    print(f"Added: parent({father}, {child}) and male({father})")

def handle_siblings(match):
    person1, person2 = match.groups()

    if person1 == person2:
        print("That's impossible! A person can't be their own sibling.")
        return

    # Check contradiction: one is parent of the other
    contradiction = list(prolog.query(f"parent('{person1}', '{person2}')")) or \
                    list(prolog.query(f"parent('{person2}', '{person1}')"))
    if contradiction:
        print("That's impossible! A parent and child cannot be siblings.")
        return

    # Check if they already share a parent
    shared_parent = list(prolog.query(
        f"parent(Z, '{person1}'), parent(Z, '{person2}'), '{person1}' \\= '{person2}'"
    ))
    if shared_parent:
        print(f"Confirmed: {person1} and {person2} are siblings (they already share a parent).")
        return

    # Ask for common parent
    parent = input(f"No shared parent found. Who is the parent of both {person1} and {person2}? ").strip()

    if not parent or parent in [person1, person2]:
        print("That's impossible! Invalid parent name.")
        return

    # Check if adding this parent would create a contradiction
    contradiction = list(prolog.query(f"parent('{person1}', '{parent}')")) or \
                    list(prolog.query(f"parent('{person2}', '{parent}')"))
    if contradiction:
        print("That's impossible! Adding this parent would cause a contradiction.")
        return

    # Assert both parent relationships
    prolog.assertz(f"parent('{parent}', '{person1}')")
    prolog.assertz(f"parent('{parent}', '{person2}')")
    print(f"Added: parent({parent}, {person1}) and parent({parent}, {person2}) — now {person1} and {person2} are siblings.")

def handle_sister(match):
    sister, sibling = match.groups()

    if sister == sibling:
        print("That's impossible! A person can't be their own sister.")
        return

    # Gender check
    is_male = list(prolog.query(f"male({sister})"))
    if is_male:
        print(f"That's impossible! {sister} is male and cannot be a sister.")
        return

    contradiction = list(prolog.query(f"parent({sister}, {sibling})")) or \
                    list(prolog.query(f"parent({sibling}, {sister})"))
    if contradiction:
        print("That's impossible! A parent and child cannot be siblings.")
        return

    prolog.assertz(f"female({sister})")

    common_parents = list(prolog.query(
        f"parent(Z, {sister}), parent(Z, {sibling}), {sister} \\= {sibling}"
    ))
    if common_parents:
        print(f"Added: female({sister}) — confirmed {sister} is the sister of {sibling}.")
        return

    parent = input(f"No shared parent found. Who is the parent of both {sister} and {sibling}? ").strip()
    if not parent or parent in [sister, sibling]:
        print("That's impossible! Invalid parent name.")
        return

    contradiction = list(prolog.query(f"parent({sister}, {parent})")) or \
                    list(prolog.query(f"parent({sibling}, {parent})"))
    if contradiction:
        print("That's impossible! Adding this parent would cause a contradiction.")
        return

    safe_assert_parent(parent, sister)
    safe_assert_parent(parent, sibling)
    print(f"Added: {sister} is the sister of {sibling}.")

def handle_mother(match):
    mother, child = match.groups()

    if mother == child:
        print("That's impossible! A person can't be their own parent.")
        return

    if check_gender_conflict(mother, expected_gender="female"):
        print(f"That's impossible! {mother} is already declared male and cannot be a mother.")
        return

    ancestor_result = list(prolog.query(f"ancestor('{child}', '{mother}')"))
    parent_result = list(prolog.query(f"parent('{child}', '{mother}')"))
    contradiction = bool(ancestor_result) or bool(parent_result) or mother == child

    if contradiction:
        print("That's impossible! That would create a contradiction.")
        print("[Debug] ancestor check:", ancestor_result)
        print("[Debug] parent check:", parent_result)
        print("[Debug] equality check:", mother == child)
        return

    safe_assert_parent(mother, child)
    if not list(prolog.query(f"female('{mother}')")):
        prolog.assertz(f"female('{mother}')")
    print(f"Added: parent({mother}, {child}) and female({mother})")

def handle_grandmother(match):
    grandmother, grandchild = match.groups()

    if grandmother == grandchild:
        print("That's impossible! A person can't be their own grandchild.")
        return

    # Gender check
    is_male = list(prolog.query(f"male('{grandmother}')"))
    if is_male:
        print(f"That's impossible! {grandmother} is male and cannot be a grandmother.")
        return

    middle = input(f"Who is the child of {grandmother} and parent of {grandchild}? ").strip()
    if not middle or middle in [grandmother, grandchild]:
        print("That's impossible! Invalid intermediate person.")
        return

    contradiction = list(prolog.query(f"parent('{grandchild}', '{middle}')")) or \
                    list(prolog.query(f"parent('{middle}', '{grandmother}')"))
    if contradiction:
        print("That's impossible! That would create a contradiction.")
        return

    # Use 'mother' instead of just 'parent' to satisfy grandmother rule
    prolog.assertz(f"mother('{grandmother}', '{middle}')")
    safe_assert_parent(middle, grandchild)
    prolog.assertz(f"female('{grandmother}')")
    print(f"Added: grandmother({grandmother}, {grandchild}) ")

def handle_child(match):
    child, parent = match.groups()
    try:
        # Prevent circular parent-child relationships
        circular = list(prolog.query(f"parent({child}, {parent})")) or \
                   list(prolog.query(f"child({parent}, {child})")) or \
                   list(prolog.query(f"{child} = {parent}"))
    except Exception:
        circular = False

    if circular:
        print(f"That's impossible! A person can't be their own parent or child.")
        return

    # Only assert the parent relationship; child will be inferred
    safe_assert_parent(parent, child)


def handle_daughter(match):
    daughter, parent = match.groups()

    if daughter == parent:
        print("That's impossible! A person can't be their own parent.")
        return

    if check_gender_conflict(daughter, expected_gender="female"):
        print(f"That's impossible! {daughter} is already declared male and cannot be a daughter.")
        return

    # Safely detect contradictions
    try:
        ancestor_result = list(prolog.query(f"ancestor('{daughter}', '{parent}')"))
        parent_result = list(prolog.query(f"parent('{daughter}', '{parent}')"))

        # Only treat as contradiction if at least one *non-empty* match
        has_contradiction = any(len(r) > 0 for r in ancestor_result + parent_result) or daughter == parent

        if has_contradiction:
            print("That's impossible! That would create a contradiction.")
            print("[Debug] ancestor check:", ancestor_result)
            print("[Debug] parent check:", parent_result)
            print("[Debug] equality check:", daughter == parent)
            return

    except Exception as e:
        print("[Error] Prolog query failed:", e)
        return

    # All clear — assert
    safe_assert_parent(parent, daughter)
    if not list(prolog.query(f"female('{daughter}')")):
        prolog.assertz(f"female('{daughter}')")
    print(f"Added: {daughter} is now the daughter of {parent}.")


def handle_uncle(match):
    uncle, niece_or_nephew = match.groups()

    if uncle == niece_or_nephew:
        print("That's impossible! A person can't be their own uncle.")
        return

    # Gender consistency
    if check_gender_conflict(uncle, expected_gender="male"):
        print(f"That's impossible! {uncle} is already declared female and cannot be an uncle.")
        return

    # Ask who is the parent of the niece/nephew
    parent = input(f"Who is the parent of {niece_or_nephew}? ").strip()
    if not parent or parent in [uncle, niece_or_nephew]:
        print("That's impossible! Invalid parent name.")
        return

    # Check if parent-child link already exists
    if not list(prolog.query(f"parent('{parent}', '{niece_or_nephew}')")):
        prolog.assertz(f"parent('{parent}', '{niece_or_nephew}')")
        print(f"Added: parent({parent}, {niece_or_nephew})")

    # Check if uncle and parent are already siblings
    if not list(prolog.query(f"sibling('{uncle}', '{parent}')")):
        prolog.assertz(f"sibling('{uncle}', '{parent}')")
        print(f"Added: sibling({uncle}, {parent})")

    # Declare male if not already declared
    if not list(prolog.query(f"male('{uncle}')")):
        prolog.assertz(f"male('{uncle}')")
        print(f"Added: male({uncle})")

    print(f"{uncle} is now the uncle of {niece_or_nephew} (via sibling of parent {parent}).")

def handle_brother(match):
    brother, sibling = match.groups()

    if brother == sibling:
        print("That's impossible! A person can't be their own brother.")
        return

    # Gender check
    is_female = list(prolog.query(f"female({brother})"))
    if is_female:
        print(f"That's impossible! {brother} is female and cannot be a brother.")
        return

    # Contradiction: parent-child relationship
    contradiction = list(prolog.query(f"parent({brother}, {sibling})")) or \
                    list(prolog.query(f"parent({sibling}, {brother})"))
    if contradiction:
        print("That's impossible! A parent and child cannot be siblings.")
        return

    prolog.assertz(f"male({brother})")

    common_parents = list(prolog.query(
        f"parent(Z, {brother}), parent(Z, {sibling}), {brother} \\= {sibling}"
    ))
    if common_parents:
        print(f"Added: male({brother}) — confirmed {brother} is the brother of {sibling}.")
        return

    parent = input(f"No shared parent found. Who is the parent of both {brother} and {sibling}? ").strip()
    if not parent or parent in [brother, sibling]:
        print("That's impossible! Invalid parent name.")
        return

    contradiction = list(prolog.query(f"parent({brother}, {parent})")) or \
                    list(prolog.query(f"parent({sibling}, {parent})"))
    if contradiction:
        print("That's impossible! Adding this parent would cause a contradiction.")
        return

    prolog.assertz(f"parent({parent}, {brother})")
    prolog.assertz(f"parent({parent}, {sibling})")
    print(f"Added: male({brother}), parent({parent}, {brother}), parent({parent}, {sibling}) — now {brother} is the brother of {sibling}.")

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

    if grandfather == grandchild:
        print("That's impossible! A person can't be their own grandchild.")
        return

    # Gender check
    is_female = list(prolog.query(f"female('{grandfather}')"))
    if is_female:
        print(f"That's impossible! {grandfather} is female and cannot be a grandfather.")
        return

    middle = input(f"Who is the child of {grandfather} and parent of {grandchild}? ").strip()
    if not middle or middle in [grandfather, grandchild]:
        print("That's impossible! Invalid intermediate person.")
        return

    contradiction = list(prolog.query(f"parent('{grandchild}', '{middle}')")) or \
                    list(prolog.query(f"parent('{middle}', '{grandfather}')"))
    if contradiction:
        print("That's impossible! That would create a contradiction.")
        return

    # Use 'father' instead of just 'parent' so it satisfies the rule grandfather(X,Y) :- father(X,Z), parent(Z,Y).
    prolog.assertz(f"father('{grandfather}', '{middle}')")
    prolog.assertz(f"parent('{middle}', '{grandchild}')")
    prolog.assertz(f"male('{grandfather}')")
    print(f"Added: father({grandfather}, {middle}), parent({middle}, {grandchild}), male({grandfather}) — grandfather({grandfather}, {grandchild}) will be inferred.")

def handle_children(match):
    children = match.groups()
    parent = children[-1]

    for child in children[:-1]:
        if child == parent:
            print(f"That's impossible! A person can't be their own parent.")
            return

        # Check for circular contradiction
        try:
            contradiction = list(prolog.query(f"parent({child}, {parent})")) or \
                            list(prolog.query(f"{child} = {parent}"))
        except Exception:
            contradiction = False

        if contradiction:
            print(f"That's impossible! Adding parent({parent}, {child}) would cause a contradiction.")
            return

        # Assert parent relationship (child is derived by rule)
        safe_assert_parent(parent, child)


def handle_son(match):
    son, parent = match.groups()

    if son == parent:
        print("That's impossible! A person can't be their own parent.")
        return

    if check_gender_conflict(son, expected_gender="male"):
        print(f"That's impossible! {son} is already declared female and cannot be a son.")
        return

    # Check for contradiction
    ancestor_result = list(prolog.query(f"ancestor('{son}', '{parent}')"))
    parent_result = list(prolog.query(f"parent('{son}', '{parent}')"))
    contradiction = bool(ancestor_result) or bool(parent_result) or son == parent

    if contradiction:
        print("That's impossible! That would create a contradiction.")
        print("[Debug] ancestor check:", ancestor_result)
        print("[Debug] parent check:", parent_result)
        print("[Debug] equality check:", son == parent)
        return

    safe_assert_parent(parent, son)
    prolog.assertz(f"male('{son}')")
    print(f"Added: {son} is now the son of {parent}.")

def handle_aunt(match):
    aunt, niece_or_nephew = match.groups()

    if aunt == niece_or_nephew:
        print("That's impossible! A person can't be their own aunt.")
        return

    if check_gender_conflict(aunt, expected_gender="female"):
        print(f"That's impossible! {aunt} is already declared male and cannot be an aunt.")
        return

    prolog.assertz(f"female('{aunt}')")

    # Step 1: Try to find an existing parent of the niece_or_nephew
    parents = list(prolog.query(f"parent(P, '{niece_or_nephew}')"))
    if parents:
        parent = parents[0]['P']
        print(f"[Info] Found existing parent of {niece_or_nephew}: {parent}")
    else:
        parent = input(f"Who is the parent of {niece_or_nephew}? ").strip()
        if not parent or parent in [aunt, niece_or_nephew]:
            print("That's impossible! Invalid parent name.")
            return
        safe_assert_parent(parent, niece_or_nephew)

    # Step 2: Check if aunt is already sibling of parent
    is_sibling = list(prolog.query(f"sibling('{aunt}', '{parent}')"))
    if not is_sibling:
        common_parent = input(f"Who is the common parent of both {aunt} and {parent}? ").strip()
        if not common_parent or common_parent in [aunt, parent, niece_or_nephew]:
            print("That's impossible! Invalid common parent name.")
            return
        safe_assert_parent(common_parent, aunt)
        safe_assert_parent(common_parent, parent)
        print(f"Added: parent({common_parent}, {aunt}), parent({common_parent}, {parent}) — now {aunt} and {parent} are siblings.")

    print(f"{aunt} is now the aunt of {niece_or_nephew} (via sibling of parent {parent}).")



patterns = [
    (r"(\w+)\s+is the father of\s+(\w+)\.?", handle_father),
    (r"(\w+)\s+and\s+(\w+)\s+are siblings\.?", handle_siblings),
    (r"(\w+)\s+is a sister of\s+(\w+)\.?", handle_sister),
    (r"(\w+)\s+is the mother of\s+(\w+)\.?", handle_mother),
    (r"(\w+)\s+is a grandmother of\s+(\w+)\.?", handle_grandmother),
    (r"(\w+)\s+is a child of\s+(\w+)\.?", handle_child),
    (r"(\w+)\s+is a daughter of\s+(\w+)\.?", handle_daughter),
    (r"(\w+)\s+is an uncle of\s+(\w+)\.?", handle_uncle),
    (r"(\w+)\s+is a brother of\s+(\w+)\.?", handle_brother),
    (r"(\w+)\s+and\s+(\w+)\s+are parents of\s+(\w+)\.?", handle_parents),
    (r"(\w+)\s+is a grandfather of\s+(\w+)\.?", handle_grandfather),
    (r"(\w+),\s*(\w+),?\s*and\s+(\w+)\s+are children of\s+(\w+)\.?", handle_children),
    (r"(\w+)\s+is a son of\s+(\w+)\.?", handle_son),
    (r"(\w+)\s+is an aunt of\s+(\w+)\.?", handle_aunt),
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
                        if "X" in query:
                        # Display each X value found
                            for result in results:
                                print(result.get("X", result))
                        else:
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