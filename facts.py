from pyswip import Prolog

class Facts():
    def add_fact(p, statement):
        try:
            p.assertz(statement)
            result = Facts.check_contradiction(p, statement)
            return result
        except Exception as e:
            print(f"Error adding fact: {e}")

    def check_contradiction(p,statement):
        try:
            contradiction = list(p.query("contradiction(X)"))
            if contradiction:
                p.retract(statement)
                print(f"Contradiction found: {statement} retracted.")
                return True
        except Exception as e:
            print(f"Error checking contradiction: {e}")
            return False

    def siblings(p,x,y):
        try:
            already_exists = bool(list(p.query("siblings({}, {})".format(x, y))))
            if already_exists:
                print("Sibling fact already exists.")
            else:
                result1 = Facts.add_fact(p,"siblings({},{})".format(x,y))
                result2 = Facts.add_fact(p,"siblings({},{})".format(y,x))
                if result1 or result2: #if either of these facts are contradictory, remove them both
                    p.retract("siblings({},{})".format(x,y))
                    p.retract("siblings({},{})".format(y,x))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting sibling fact: {e}")

    def son(p,x,y):
        try:
            already_exists = bool(list(p.query("son({}, {})".format(x, y))))
            if already_exists:
                print("Son fact already exists.")
            else:
                result1 = Facts.add_fact(p,"male({})".format(x))
                result2 = Facts.add_fact(p,"parent({},{})".format(y,x))
                if result1 or result2:
                    p.retract("parent({},{})".format(y,x))
                    p.retract("male({})".format(x))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting son fact: {e}")

    def sister(p, x, y):
        try:
            already_exists = bool(list(p.query("sister({}, {})".format(x, y))))
            if already_exists:
                print("Sister fact already exists.")
            else:
                result1 = Facts.add_fact(p,"siblings({},{})".format(x,y))
                result2 = Facts.add_fact(p,"female({})".format(x))
                result3 = Facts.add_fact(p,"siblings({},{})".format(y,x))
                if result1 or result2 or result3:
                    p.retract("siblings({},{})".format(x,y))
                    p.retract("female({})".format(x))
                    p.retract("siblings({},{})".format(y,x))
                if not result1 and not result2 and not result3:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting sister fact: {e}")


    def grandmother(p,x,y):
        try:
            already_exists = bool(list(p.query("grandmother({}, {})".format(x, y))))
            if already_exists:
                print("Grandmother fact already exists.")
            else:
                result1 = Facts.add_fact(p,"grandmother({},{})".format(x,y))
                result2 = Facts.add_fact(p,"female({})".format(x))
                if result1 or result2:
                    p.retract("grandmother({},{})".format(x,y))
                    p.retract("female({})".format(x))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting grandmother fact: {e}")

    def grandfather(p,x,y):
        try:
            already_exists = bool(list(p.query("grandfather({}, {})".format(x, y))))
            if already_exists:
                print("Grandfather fact already exists.")
            else:
                result1 = Facts.add_fact(p,"grandfather({},{})".format(x,y))
                result2 = Facts.add_fact(p,"male({})".format(x))
                if result1 or result2:
                    p.retract("grandfather({},{})".format(x,y))
                    p.retract("male({})".format(x))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting grandfather fact: {e}")

    def child(p,x,y):
        try:
            already_exists = bool(list(p.query("parent({}, {})".format(y, x))))
            if already_exists:
                print("Child fact already exists.")
            else:
                result = Facts.add_fact(p,"parent({},{})".format(y,x))
                if result:
                    p.retract("parent({},{})".format(y,x))
                if not result:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting child fact: {e}")

    def daughter(p,x,y):
        try:
            already_exists = bool(list(p.query("daughter({}, {})".format(x, y))))
            if already_exists:
                print("Daughter fact already exists.")
            else:
                result1 = Facts.add_fact(p,"female({})".format(x))
                result2 = Facts.add_fact(p,"parent({},{})".format(y,x))
                if result1 or result2:
                    p.retract("female({})".format(x))
                    p.retract("parent({},{})".format(y,x))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting daughter fact: {e}")

    def brother(p,x,y):
        try:
            already_exists = bool(list(p.query("brother({}, {})".format(x, y))))
            if already_exists:
                print("Brother fact already exists.")
            else:
                result1 = Facts.add_fact(p,"male({})".format(x))
                result2 = Facts.add_fact(p,"siblings({},{})".format(x,y))
                result3 = Facts.add_fact(p,"siblings({},{})".format(y,x))
                if result1 or result2 or result3:
                    p.retract("male({})".format(x))
                    p.retract("siblings({},{})".format(x,y))
                    p.retract("siblings({},{})".format(y,x))
                if not result1 and not result2 and not result3:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting brother fact: {e}")

    def uncle(p,x,y):
        try:
            already_exists = bool(list(p.query("uncle({}, {})".format(x, y))))
            if already_exists:
                print("Uncle fact already exists.")
            else:
                result1 = Facts.add_fact(p,"uncle({},{})".format(x,y))
                result2 = Facts.add_fact(p,"male({})".format(x))
                if result1 or result2:
                    p.retract("uncle({},{})".format(x,y))
                    p.retract("male({})".format(x))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting uncle fact: {e}")

    def aunt(p,x,y):
        try:
            already_exists = bool(list(p.query("aunt({}, {})".format(x, y))))
            if already_exists:
                print("Aunt fact already exists.")
            else:
                result1 = Facts.add_fact(p,"aunt({},{})".format(x,y))
                result2 = Facts.add_fact(p,"female({})".format(x))
                if result1 or result2:
                    p.retract("aunt({},{})".format(x,y))
                    p.retract("female({})".format(x))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting aunt fact: {e}")

    def mother(p,x,y):
        try:
            already_exists = bool(list(p.query("mother({}, {})".format(x, y))))
            if already_exists:
                print("Mother fact already exists.")
            else:
                result1 = Facts.add_fact(p,"female({})".format(x))
                result2 = Facts.add_fact(p,"parent({},{})".format(x,y))
                if result1 or result2:
                    p.retract("female({})".format(x))
                    p.retract("parent({},{})".format(x,y))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting mother fact: {e}")

    def father(p,x,y):
        try:
            already_exists = bool(list(p.query("father({}, {})".format(x, y))))
            if already_exists:
                print("Father fact already exists.")
            else:
                result1 = Facts.add_fact(p,"male({})".format(x))
                result2 = Facts.add_fact(p,"parent({},{})".format(x,y))
                if result1 or result2:
                    p.retract("parent({},{})".format(x,y))
                    p.retract("male({})".format(x))
                if not result1 and not result2:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting father fact: {e}")

    def parents(p,x,y,z):
        try:
            already_exists = bool(list(p.query("parents_of({},{},{})".format(x,y,z))))
            if already_exists:
                print("Parents fact already exists.")
            else:
                result1 = Facts.add_fact(p,"parents_of({},{},{})".format(x,y,z))
                result2 = Facts.add_fact(p,"parent({},{})".format(x,z))
                result3 = Facts.add_fact(p,"parent({},{})".format(y,z))
                if result1 or result2 or result3:
                    p.retract("parents_of({},{},{})".format(x,y,z))
                    p.retract("parent({},{})".format(x,z))
                    p.retract("parent({},{})".format(y,z))
                if not result1 and not result2 and not result3:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting parents fact: {e}")

    def children(p,x,y,z,a):
        try:
            already_exists = bool(list(p.query("parent({}, {})".format(a,x))))
            if already_exists:
                print("Children fact already exists.")
            else:
                result1 = Facts.add_fact(p,"parent({},{})".format(a,x))
                result2 = Facts.add_fact(p,"parent({},{})".format(a,y))
                result3 = Facts.add_fact(p,"parent({},{})".format(a,z))
                if result1 or result2 or result3:
                    p.retract("parent({},{})".format(a,x))
                    p.retract("parent({},{})".format(a,y))
                    p.retract("parent({},{})".format(a,z))
                if not result1 and not result2 and not result3:
                    print("OK! I learned something.")
        except Exception as e:
            print(f"Error asserting children fact: {e}")

    # function only applies to the two arguement statements
    def execute_typeof_family(family,x,y,p):
        if family == "siblings":
            Facts.siblings(p,x,y)
        elif family == "son":
            Facts.son(p,x,y)
        elif family == "sister":
            print("Executing sister fact")
            Facts.sister(p,x,y)
        elif family == "grandmother":
            Facts.grandmother(p,x,y)
        elif family == "grandfather":
            Facts.grandfather(p,x,y)
        elif family == "child":
            Facts.child(p,x,y)
        elif family == "daughter":
            Facts.daughter(p,x,y)
        elif family == "grandfather":
            Facts.grandfather(p,x,y)
        elif family == "brother":
            Facts.brother(p,x,y)
        elif family == "uncle":
            Facts.uncle(p,x,y)
        elif family == "aunt":
            Facts.aunt(p,x,y)
        elif family == "mother":
            Facts.mother(p,x,y)
        elif family == "father":
            Facts.father(p,x,y)