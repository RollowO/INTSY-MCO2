from pyswip import Prolog
class Query():

    def query_siblings( x, y, p):
        try:
            results = bool(list(p.query("siblings({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying siblings: {e}")

    def query_son( x, y, p):
        try:
            results = bool(list(p.query("son({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying son: {e}")

    def query_sister( x, y, p):
        try:
            results = bool(list(p.query("sister({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying sister: {e}")

    def query_grandmother( x, y, p):
        try:
            results = bool(list(p.query("grandmother({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying grandmother: {e}")

    def query_grandfather( x, y, p):
        try:
            results = bool(list(p.query("grandfather({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying grandfather: {e}")

    def query_child( x, y, p):
        try:
            results = bool(list(p.query("child({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying child: {e}")

    def query_daughter( x, y, p):
        try:
            results = bool(list(p.query("daughter({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying daughter: {e}")

    def query_brother( x, y, p):
        try:
            results = bool(list(p.query("brother({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying brother: {e}")

    def query_uncle( x, y, p):
        try:
            results = bool(list(p.query("uncle({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying uncle: {e}")

    def query_aunt( x, y, p):
        try:
            results = bool(list(p.query("aunt({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying aunt: {e}")

    def query_mother( x, y, p):
        try:
            results = bool(list(p.query("mother({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying mother: {e}")

    def query_father( x, y, p):
        try:
            results = bool(list(p.query("father({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying father: {e}")

    def query_parents( x, y, z, p):
        try:
            results = bool(list(p.query("parents({},{},{})".format(x,y,z))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying parents: {e}")

    def query_children( x, y, z, a, p):
        try:
            results = bool(list(p.query("children({},{},{},{})".format(x,y,z,a))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying children: {e}")

    # LIST QUERIES, WHO ARE X OF Y?
    def find_siblings( x, p):
        results = list(p.query("siblings({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_sisters( x, p):
        results = list(p.query("sister({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_brothers( x, p):
        results = list(p.query("brother({}, X)".format(x)))
        return [result['X'] for result in results]

    def find_parents( x, p):
        results = list(p.query("parents({}, X, Y)".format(x)))
        return [(result['X'], result['Y']) for result in results]

    def find_mother( x, p):
        results = list(p.query("mother({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_father( x, p):
        results = list(p.query("father({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_daughters( x, p):
        results = list(p.query("daughter({}, X)".format(x)))
        return [result['X'] for result in results]

    def find_sons( x, p):
        results = list(p.query("son({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_children( x, p):
        results = list(p.query("children({}, X, Y, Z)".format(x)))
        return [(result['X'], result['Y'], result['Z']) for result in results]

    def execute_is_x_typeof_y(typeof,x,y,p):
        # is nameOne a/an/the ___ of nameTwo?
        todo()

    
