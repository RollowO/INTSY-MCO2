from pyswip import Prolog

new_knowledge = "OK! I learned something"
error_knowledge = "Oops! Something went wrong."
class Facts():
    def add_fact(p, fact):
        try:
            p.assertz(fact)

            # Check for contradictions
            contradictions = list(p.query("contradiction(Reason)"))
            #print("Contradictions found:", contradictions)  # Debug
            if contradictions:
                # If a contradiction is found, remove fact
                p.retract(fact)
                return False
            return True,
        except Exception as e:
            return f"Error: {str(e)}"



    def siblings(p,x,y):
        try:
            already_exists = bool(list(p.query("siblings('{}', '{}')".format(x, y))))

            result1 = Facts.add_fact(p,"siblings('{}','{}')".format(x,y))
            result2 = Facts.add_fact(p,"siblings('{}','{}')".format(y,x))
            if result1 and result2:
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting sibling fact: {e}")

    def son(p,x,y):
        try:
            result1 = Facts.add_fact(p,"male('{}')".format(x))
            result2 = Facts.add_fact(p,"parent('{}','{}')".format(y,x))
            result3 = Facts.add_fact(p,"child('{}','{}')".format(x,y))

            if result1 and result2 and result3:
                print(new_knowledge)
            else:
                print(error_knowledge)

                  
        except Exception as e:
            print(f"Error asserting son fact: {e}")

    def sister(p, x, y):
        try:

            result1 = Facts.add_fact(p,"siblings('{}','{}')".format(x,y))
            result3 = Facts.add_fact(p,"siblings('{}','{}')".format(y,x))
            result2 = Facts.add_fact(p,"female('{}')".format(x))
            if result1 and result2 and result3:
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting sister fact: {e}")


    def grandmother(p,x,y):
        try:
            result1 = Facts.add_fact(p,"grandmother('{}','{}')".format(x,y))
            result2 = Facts.add_fact(p,"grandchild('{}','{}')".format(y,x))
            result3 = Facts.add_fact(p,"female('{}')".format(x))
            if result1 and result2 and result3:
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting grandmother fact: {e}")

    def grandfather(p,x,y):
        try:
            result1 = Facts.add_fact(p,"grandfather('{}','{}')".format(x,y))
            result3 = Facts.add_fact(p,"grandchild('{}','{}')".format(y,x))
            result2 = Facts.add_fact(p,"male('{}')".format(x))
            if(result1 and result2 and result3):
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting grandfather fact: {e}")

    def child(p,x,y):
        try:
            result2 = Facts.add_fact(p,"child('{}','{}')".format(x,y))
            result = Facts.add_fact(p,"parent('{}','{}')".format(y,x))
            if(result and result2):
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting child fact: {e}")

    def daughter(p,x,y):
        try:

            result1 = Facts.add_fact(p,"child('{}','{}')".format(x,y))
            result2 = Facts.add_fact(p,"parent('{}','{}')".format(y,x))
            result3 = Facts.add_fact(p,"female('{}')".format(x))
            if result1 and result3 and result2:
                print(new_knowledge)
            else:
                print(error_knowledge)
                 
        except Exception as e:
            print(f"Error asserting daughter fact: {e}")

    def brother(p,x,y):
        try:
            result1 = Facts.add_fact(p,"siblings('{}','{}')".format(x,y))
            result2 = Facts.add_fact(p,"siblings('{}','{}')".format(y,x))
            result3 = Facts.add_fact(p,"male('{}')".format(x))
            if result1 and result2 and result3:
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting brother fact: {e}")

    def uncle(p,x,y):
        try:
            result1 = Facts.add_fact(p,"uncle('{}','{}')".format(x,y))
            result2 = Facts.add_fact(p,"male('{}')".format(x))
            if result1 and result2:
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting uncle fact: {e}")

    def aunt(p,x,y):
        try:
            result1 = Facts.add_fact(p,"aunt('{}','{}')".format(x,y))
            result2 = Facts.add_fact(p,"female('{}')".format(x))
            if result1 and result2:
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting aunt fact: {e}")

    def mother(p,x,y):
        try:
            result1 = Facts.add_fact(p,"female('{}')".format(x))
            result2 = Facts.add_fact(p,"parent('{}','{}')".format(x,y))
            result3 = Facts.add_fact(p,"child('{}','{}')".format(y,x))
            if result1 and result2 and result3:
                print(new_knowledge)
            else:
                print(error_knowledge)

              
        except Exception as e:
            print(f"Error asserting mother fact: {e}")

    def father(p,x,y):
        try:
            result2 = Facts.add_fact(p,"parent('{}','{}')".format(x,y))
            result3 = Facts.add_fact(p,"child('{}','{}')".format(y,x))
            result1 = Facts.add_fact(p,"male('{}')".format(x))
            if result1 and result2 and result3:
                print(new_knowledge)
            else:
                print(error_knowledge)
                
        except Exception as e:
            print(f"Error asserting father fact: {e}")

    def parents(p,x,y,z):
        try:
            result4 = add_fact(p,"child('{}','{}')".format(z,x))
            result1 = add_fact(p,"child('{}','{}')".format(z,y))
            result2 = Facts.add_fact(p,"parent('{}','{}')".format(x,z))
            result3 = Facts.add_fact(p,"parent('{}','{}')".format(y,z))
            if(result1 and result2 and result3 and result4):
                print(new_knowledge)
            else:
                print(error_knowledge)
        except Exception as e:
            print(f"Error asserting parents fact: {e}")

    def children(p,x,y,z,a):
        try:
            result1 = Facts.add_fact(p,"parent('{}','{}')".format(a,x))
            result2 = Facts.add_fact(p,"parent('{}','{}')".format(a,y))
            result3 = Facts.add_fact(p,"parent('{}','{}')".format(a,z))

            result4 = Facts.add_fact(p,"child('{}','{}')".format(x,a))
            result5 = Facts.add_fact(p,"child('{}','{}')".format(y,a))
            result6 = Facts.add_fact(p,"child('{}','{}')".format(z,a))
            if result1 and result2 and result3 and result4 and result5 and result6:
                print(new_knowledge)
            else:
                print(error_knowledge)
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