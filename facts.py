from pyswip import Prolog

class Facts():
    def siblings(p,x,y):
        try:
            p.assertz("siblings({},{})".format(x,y))
            p.assertz("siblings({},{})".format(y,x))
            print("Sibling fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting sibling fact: {e}")

    def son(p,x,y):
        try:
            p.assertz("son({},{})".format(x,y))
            p.assertz("male({})".format(x))
            p.assertz("parent({},{})".format(x,y))
            print("Son fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting son fact: {e}")

    def sister(p, x, y):
        try:
            p.assertz(f"siblings({x}, {y})")
            p.assertz(f"female({x})")
            p.assertz(f"siblings({y}, {x})")
            print("Sister fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting sister fact: {e}")


    def grandmother(p,x,y):
        try:
            p.assertz("grandmother({},{})".format(x,y))
            p.assertz("female({})".format(x))
            print("Grandmother fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting grandmother fact: {e}")

    def grandfather(p,x,y):
        try:
            p.assertz("grandfather({},{})".format(x,y))
            p.assertz("male({})".format(x))
            print("Grandfather fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting grandfather fact: {e}")

    def child(p,x,y):
        try:
            p.assertz("parent({},{})".format(y,x))
            print("Child fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting child fact: {e}")

    def daughter(p,x,y):
        try:
            p.assertz("daughter({},{})".format(x,y))
            p.assertz("female({})".format(x))
            p.assertz("parent({},{})".format(x,y))
            print("Daughter fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting daughter fact: {e}")

    def brother(p,x,y):
        try:
            p.assertz("male({})".format(x))
            p.assertz("siblings({},{})".format(x,y))
            p.assertz("siblings({},{})".format(y,x))
            print("Brother fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting brother fact: {e}")

    def uncle(p,x,y):
        try:
            p.assertz("uncle({},{})".format(x,y))
            p.assertz("male({})".format(x))
            print("Uncle fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting uncle fact: {e}")

    def aunt(p,x,y):
        try:
            p.assertz("aunt({},{})".format(x,y))
            p.assertz("female({})".format(x))
            print("Aunt fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting aunt fact: {e}")

    def mother(p,x,y):
        try:
            p.assertz("mother({},{})".format(x,y))
            p.assertz("female({})".format(x))
            p.assertz("parent({},{})".format(x,y))
            print("Mother fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting mother fact: {e}")

    def father(p,x,y):
        try:
            p.assertz("father({},{})".format(x,y))
            p.assertz("male({})".format(x))
            p.assertz("parent({},{})".format(x,y))
            print("Father fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting father fact: {e}")

    def parents(p,x,y,z):
        try:
            p.assertz("parents_of({},{},{})".format(x,y,z))
            p.assertz("parent({},{})".format(x,z))
            p.assertz("parent({},{})".format(y,z))
            print("Parents fact asserted successfully.")
        except Exception as e:
            print(f"Error asserting parents fact: {e}")

    def children(p,x,y,z,a):
        try:
            p.assertz("parent({},{})".format(a,x))
            p.assertz("parent({},{})".format(a,y))
            p.assertz("parent({},{})".format(a,z))
            print("Children fact asserted successfully.")
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