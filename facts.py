from pyswip import Prolog

class Facts():
    
    def siblings(p,x,y):
        p.assertz("sibling({},{})".format(x,y))

    def son(p,x,y):
        p.assertz("son({},{})".format(x,y))
    def sister(p,x,y):
        p.assertz("sister({},{})".format(x,y))
    def grandmother(p,x,y):
        p.assertz("grandmother({},{})".format(x,y))
        
    def grandfather(p,x,y):
        p.assertz("grandfather({},{})".format(x,y))
    def child(p,x,y):
        p.assertz("child({},{})".format(x,y))
    def daughter(p,x,y):
        p.assertz("daughter({},{})".format(x,y))
    def grandfather(p,x,y):
        p.assertz("grandfather({},{})".format(x,y))
    def brother(p,x,y):
        p.assertz("brother({},{})".format(x,y))
    def uncle(p,x,y):
        p.assertz("uncle({},{})".format(x,y))
    def aunt(p,x,y):
        p.assertz("aunt({},{})".format(x,y))
    def mother(p,x,y):
        p.assertz("mother({},{})".format(x,y))
    def father(p,x,y):
        p.assertz("father({},{})".format(x,y))
    def parents(p,x,y,z):
        p.assertz("parents({},{},{})").format(x,y,z)

    def children(p,x,y,z,a):
        p.assertz("children({},{},{},{})".format(x,y,z,a))
