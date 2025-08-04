from pyswip import Prolog
class Query():

    def query_siblings(self, x, y, p):
        try:
            results = bool(list(p.query("siblings({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying siblings: {e}")

    def query_son(self, x, y, p):
        try:
            results = bool(list(p.query("son({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying son: {e}")

    def query_sister(self, x, y, p):
        try:
            results = bool(list(p.query("sister({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying sister: {e}")

    def query_grandmother(self, x, y, p):
        try:
            results = bool(list(p.query("grandmother({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying grandmother: {e}")

    def query_grandfather(self, x, y, p):
        try:
            results = bool(list(p.query("grandfather({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying grandfather: {e}")

    def query_child(self, x, y, p):
        try:
            results = bool(list(p.query("child({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying child: {e}")

    def query_daughter(self, x, y, p):
        try:
            results = bool(list(p.query("daughter({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying daughter: {e}")

    def query_brother(self, x, y, p):
        try:
            results = bool(list(p.query("brother({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying brother: {e}")

    def query_uncle(self, x, y, p):
        try:
            results = bool(list(p.query("uncle({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying uncle: {e}")

    def query_aunt(self, x, y, p):
        try:
            results = bool(list(p.query("aunt({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying aunt: {e}")

    def query_mother(self, x, y, p):
        try:
            results = bool(list(p.query("mother({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying mother: {e}")

    def query_father(self, x, y, p):
        try:
            results = bool(list(p.query("father({}, {})".format(x, y))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying father: {e}")

    def query_parents(self, x, y, z, p):
        try:
            results = bool(list(p.query("parents({},{},{})".format(x,y,z))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying parents: {e}")

    def query_children(self, x, y, z, a, p):
        try:
            results = bool(list(p.query("children({},{},{},{})".format(x,y,z,a))))
            if results:
                return "Yes"
            else:
                return "No"
        except Exception as e:
            print(f"Error querying children: {e}")

    # LIST QUERIES, WHO ARE X OF Y?
    def find_siblings(self, x, p):
        results = list(p.query("siblings({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_sisters(self, x, p):
        results = list(p.query("sister({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_brothers(self, x, p):
        results = list(p.query("brother({}, X)".format(x)))
        return [result['X'] for result in results]

    def find_parents(self, x, p):
        results = list(p.query("parents({}, X, Y)".format(x)))
        return [(result['X'], result['Y']) for result in results]

    def find_mother(self, x, p):
        results = list(p.query("mother({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_father(self, x, p):
        results = list(p.query("father({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_daughters(self, x, p):
        results = list(p.query("daughter({}, X)".format(x)))
        return [result['X'] for result in results]

    def find_sons(self, x, p):
        results = list(p.query("son({}, X)".format(x)))
        return [result['X'] for result in results]
    
    def find_children(self, x, p):
        results = list(p.query("children({}, X, Y, Z)".format(x)))
        return [(result['X'], result['Y'], result['Z']) for result in results]