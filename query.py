from pyswip import Prolog
class Query():

    def query_siblings( x, y, p):
        try:
            results = bool(list(p.query("siblings({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying siblings: {e}")

    def query_son( x, y, p):
        try:
            results = bool(list(p.query("son({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying son: {e}")

    def query_sister( x, y, p):
        try:
            results = bool(list(p.query("sister({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying sister: {e}")

    def query_grandmother( x, y, p):
        try:
            results = bool(list(p.query("grandmother({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying grandmother: {e}")

    def query_grandfather( x, y, p):
        try:
            results = bool(list(p.query("grandfather({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying grandfather: {e}")

    def query_child( x, y, p):
        try:
            results = bool(list(p.query("child({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying child: {e}")

    def query_daughter( x, y, p):
        try:
            results = bool(list(p.query("daughter({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying daughter: {e}")

    def query_brother( x, y, p):
        try:
            results = bool(list(p.query("brother({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying brother: {e}")

    def query_uncle( x, y, p):
        try:
            results = bool(list(p.query("uncle({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying uncle: {e}")

    def query_aunt( x, y, p):
        try:
            results = bool(list(p.query("aunt({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying aunt: {e}")

    def query_mother( x, y, p):
        try:
            results = bool(list(p.query("mother({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying mother: {e}")

    def query_father( x, y, p):
        try:
            results = bool(list(p.query("father({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying father: {e}")

    def query_parents( x, y, z, p):
        try:
            results = bool(list(p.query("parents({},{},{})".format(x,y,z))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying parents: {e}")

    def query_children( x, y, z, a, p):
        try:
            results = bool(list(p.query("children({},{},{},{})".format(x,y,z,a))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying children: {e}")

    def query_relatives( x, y, p):
        try:
            results = bool(list(p.query("relatives({}, {})".format(x, y))))
            if results:
                print("Yes")
            else:
                print("No")
        except Exception as e:
            print(f"Error querying relatives: {e}")

    # LIST QUERIES, WHO ARE X OF Y?
    def find_siblings( x, p):
        results = list(p.query("siblings(X, {})".format(x)))
        print("Sibling/s of", x + ":")
        for result in results:
            print(result["X"])
    
    def find_sisters( x, p):
        results = list(p.query("sister(X, {})".format(x)))
        print("Sister/s of", x + ":")
        for result in results:
            print(result["X"])
    
    def find_brothers( x, p):
        results = list(p.query("brother(X, {})".format(x)))
        print("Brother/s of", x + ":")
        for result in results:
            print(result["X"])

    def find_parents( x, p):
        results = list(p.query("parents(X, Y, {})".format(x)))
        print("Parent/s of", x + ":")
        for result in results:
            print(result["X"])
            print(result["Y"])

    def find_mother( x, p):
        results = list(p.query("mother(X, {})".format(x)))
        print("Mother of", x + ":")
        for result in results:
            print(result["X"])
    
    def find_father( x, p):
        results = list(p.query("father(X, {})".format(x)))
        print("Father of", x + ":")
        for result in results:
            print(result["X"])
    
    def find_daughters( x, p):
        results = list(p.query("daughter(X, {})".format(x)))
        print("Daughter/s of", x + ":")
        for result in results:
            print(result["X"])

    def find_sons( x, p):
        results = list(p.query("son(X, {})".format(x)))
        print("Son/s of", x + ":")
        for result in results:
            print(result["X"])
    
    def find_children(x, p):
        results = list(p.query("children(X, Y, Z, {})".format(x)))
        print("Children of", x + ":")
        for result in results:
            print(result["X"])
            print(result["Y"])
            print(result["Z"])


            

    def execute_is_x_typeof_y(typeof,x,y,p):
        # is nameOne a/an/the ___ of nameTwo?
        if typeof =="sister":
            return Query.query_sister(x, y, p)
        elif typeof == "brother":
            return Query.query_brother(x, y, p)
        elif typeof == "son":
            return Query.query_son(x, y, p)
        elif typeof == "daughter":
            return Query.query_daughter(x, y, p)
        elif typeof == "grandmother":
            return Query.query_grandmother(x, y, p)
        elif typeof == "grandfather":
            return Query.query_grandfather(x, y, p)
        elif typeof == "uncle":
            return Query.query_uncle(x, y, p)
        elif typeof == "aunt":
            return Query.query_aunt(x, y, p)
        elif typeof == "mother":
            return Query.query_mother(x, y, p)
        elif typeof == "father":
            return Query.query_father(x, y, p)
        elif typeof == "child":
            return Query.query_child(x, y, p)

    def execute_relations_of_x(typeof,x,p):
        #Who are the ___ of ____?
        if typeof == "siblings":
            return Query.find_siblings(x, p)
        elif typeof == "sisters":
            return Query.find_sisters(x, p)
        elif typeof == "brothers":
            return Query.find_brothers(x, p)
        elif typeof == "parents":
            return Query.find_parents(x, p)
        elif typeof == "mother":
            return Query.find_mother(x, p)
        elif typeof == "father":
            return Query.find_father(x, p)
        elif typeof == "daughters":
            return Query.find_daughters(x, p)
        elif typeof == "sons":
            return Query.find_sons(x, p)
        elif typeof == "children":
            return Query.find_children(x, p)