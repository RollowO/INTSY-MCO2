from pyswip import Prolog

class Facts():
    
    def siblings(p,x,y):
        try:
            p.assertz("sibling({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting sibling fact: {e}")

    def son(p,x,y):
        try:
            p.assertz("son({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting son fact: {e}")

    def sister(p,x,y):
        try:
            p.assertz("sister({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting sister fact: {e}")

    def grandmother(p,x,y):
        try:
            p.assertz("grandmother({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting grandmother fact: {e}")

    def grandfather(p,x,y):
        try:
            p.assertz("grandfather({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting grandfather fact: {e}")

    def child(p,x,y):
        try:
            p.assertz("child({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting child fact: {e}")

    def daughter(p,x,y):
        try:
            p.assertz("daughter({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting daughter fact: {e}")

    def grandfather(p,x,y):
        try:
            p.assertz("grandfather({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting grandfather fact: {e}")

    def brother(p,x,y):
        try:
            p.assertz("brother({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting brother fact: {e}")

    def uncle(p,x,y):
        try:
            p.assertz("uncle({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting uncle fact: {e}")

    def aunt(p,x,y):
        try:
            p.assertz("aunt({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting aunt fact: {e}")

    def mother(p,x,y):
        try:
            p.assertz("mother({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting mother fact: {e}")

    def father(p,x,y):
        try:
            p.assertz("father({},{})".format(x,y))
        except Exception as e:
            print(f"Error asserting father fact: {e}")

    def parents(p,x,y,z):
        try:
            p.assertz("parents({},{},{})".format(x,y,z))
        except Exception as e:
            print(f"Error asserting parents fact: {e}")

    def children(p,x,y,z,a):
        try:
            p.assertz("children({},{},{},{})".format(x,y,z,a))
        except Exception as e:
            print(f"Error asserting children fact: {e}")

    # function only applies to the two arguement statements
    def execute_typeof_family(family,x,y,p):
        if family == "sister":
        
        elif family == "brother":
