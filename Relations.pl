:- dynamic male/1.
:- dynamic female/1.
:- dynamic parent/2.
:- dynamic child/2.
:- dynamic grandparent/2.
:- dynamic grandchild/2.
:- dynamic sibling/2.
:- dynamic uncle/2.
:- dynamic aunt/2.
:- dynamic cousin/2.
:- dynamic relative/2.

% parents
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).


% children
child(X,Y) :- parent(Y,X), X \= Y.
son(X,Y) :- child(X,Y), male(X), X \= Y.
daughter(X,Y) :- child(X,Y), female(X), X \= Y.


%  grandparents | A is subbed to any value
grandfather(X,Y) :- male(X), parent(X,A), parent(A,Y).
grandmother(X,Y) :- female(X), parent(X,A), parent(A,Y).
grandparent(X,Y) :- parent(X,P), parent(P,Y), X \= Y.

grandson(X, Y) :- grandchild(X, Y), male(X).
granddaughter(X, Y) :- grandchild(X, Y), female(X).
grandchild(X, Y) :- parent(P, X), parent(Y, P), X \= Y.

% siblings
siblings(X,Y) :- child(X,P), child(Y,P), X \= Y.
brother(X,Y) :- siblings(X,Y), male(X), X \= Y.
sister(X,Y) :- siblings(X,Y), female(X), X\= Y.

% relatives
uncle(X,Y) :- brother(X,P), child(Y,P), X\=Y.
aunt(X,Y) :- sister(X,P), child(Y,P), X \= Y.

relative(X, Y) :- parent(X, Y).    
relative(X, Y) :- parent(Y, X).     
relative(X, Y) :- sibling(X, Y).   
relative(X, Y) :- grandparent(X, Y). 
relative(X, Y) :- grandchild(X, Y). 
relative(X, Y) :- uncle(X, Y).  
relative(X, Y) :- aunt(X, Y).     
relative(X, Y) :- cousin(X, Y).  

% positions-ish
husband(X, Y) :- spouse(X, Y), male(X).
wife(X, Y) :- spouse(X, Y), female(X).
spouse(X, Y) :- parent(X, C), parent(Y, C), X \= Y.

% Atoms with Inferences
uncle(X, Y) :- siblings(X, Z), parent(Z, Y), male(X).
aunt(X, Y) :- siblings(X, Z), parent(Z, Y), female(X).

nephew(X, Y) :- siblings(Z, Y), parent(Z, X), male(X).
niece(X, Y) :- siblings(Z, Y), parent(Z, X), female(X).

cousin(X, Y) :- child(X, W), child(Y, Z), siblings(W, Z), X \= Y, W \= Z.

% Contradictions
contradiction(circular_parent) :- parent(X, Y), parent(Y, X).                      
contradiction(circular_grandparent) :- grandparent(X, Y), grandparent(Y, X).       
contradiction(circular_child) :- child(X, Y), child(Y, X).                        
contradiction(circular_uncle) :- uncle(X, Y), uncle(Y, X).                       
contradiction(circular_aunt) :- aunt(X, Y), aunt(Y, X).                           
contradiction(circular_niece) :- niece(X, Y), niece(Y, X).                       
contradiction(circular_nephew) :- nephew(X, Y), nephew(Y, X).                       

contradiction(parent_grandchild) :- parent(X, Y), parent(Y, Z), parent(Z, X).      

contradiction(self_child) :- child(X,X).                                          
contradiction(self_parent) :- parent(X, X).                                       
contradiction(self_cousin) :- cousin(X, X).                                      
contradiction(self_grandparent) :- grandparent(X, X).                              
contradiction(self_sibling) :- siblings(X, X).                                      
contradiction(self_uncle) :- uncle(X, X).                                        
contradiction(self_aunt) :- aunt(X, X).                                           
contradiction(self_nephew) :- nephew(X, X).                                     
contradiction(self_niece) :- niece(X, X).                                        
contradiction(self_spouse) :- spouse(X, X).                                        
contradiction(self_child) :- child(X, X).                                         
contradiction(self_grandchild) :- grandchild(X, X).                              

contradiction(sibling_and_parent) :- siblings(X, Y), parent(X, Y).                  

contradiction(gender_conflict) :- male(X), female(X).                             
contradiction(parent_gender_mismatch) :- parent(X, Y), male(X), mother(X, Y).    
contradiction(parent_gender_mismatch) :- parent(X, Y), female(X), father(X, Y).   
contradiction(child_gender_mismatch) :- son(X, Y), female(X), parent(Y, X).     
contradiction(child_gender_mismatch) :- daughter(X, Y), male(X), parent(Y, X).     
contradiction(parent_gender_mismatch) :- father(X, Y), mother(X, Y).             

contradiction(incest_parent_child) :- parent(X, Y), (husband(X, Y) ; wife(X, Y)).                                     
contradiction(incest_sibling) :- siblings(X, Y), (husband(X, Y) ; wife(X, Y)).                                         
contradiction(incest_grandparent) :- grandparent(X, Y), (husband(X, Y) ; wife(X, Y)).                                 
contradiction(incest_niece_nephew_parent) :- parent(X, Y), (uncle(Y, X) ; aunt(Y, X) ; niece(Y, X) ; nephew(Y, X)).   
contradiction(incest_sibling_extended) :- siblings(X, Y), (uncle(X, Y) ; aunt(X, Y) ; niece(X, Y) ; nephew(X, Y)).     

% Family Contradiction

contradiction(cousin_sibling_mismatch) :- cousin(X,Y), siblings(Y,X).            
contradiction(cousin_child_mismatch) :- cousin(X,Y), child(Y,X).                      
contradiction(cousin_parent_mismatch) :- cousin(X,Y), parent(Y,X).                   
contradiction(cousin_grandparent_mismatch) :- cousin(X,Y), grandparent(Y,X).       
contradiction(cousin_uncle_mismatch) :- cousin(X,Y), uncle(Y,X).                     
contradiction(cousin_aunt_mismatch) :- cousin(X,Y), aunt(Y,X).                      

contradiction(cousin_sibling_mismatch) :- cousin(X,Y), siblings(X,Y).                
contradiction(cousin_child_mismatch) :- cousin(X,Y), child(X,Y).                    
contradiction(cousin_parent_mismatch) :- cousin(X,Y), parent(X,Y).                
contradiction(cousin_grandparent_mismatch) :- cousin(X,Y), grandparent(X,Y).        
contradiction(cousin_uncle_mismatch) :- cousin(X,Y), uncle(X,Y).                     
contradiction(cousin_aunt_mismatch) :- cousin(X,Y), aunt(X,Y).                     

contradiction(sibling_child_mismatch) :- siblings(X,Y), child(Y,X).                   
contradiction(sibling_parent_mismatch) :- siblings(X,Y), parent(Y,X).               
contradiction(sibling_grandparent_mismatch) :- siblings(X,Y), grandparent(Y,X).      
contradiction(sibling_uncle_mismatch) :- siblings(X,Y), uncle(Y,X).                   
contradiction(sibling_aunt_mismatch) :- siblings(X,Y), aunt(Y,X).                     

contradiction(sibling_child_mismatch) :- siblings(X,Y), child(X,Y).                  
contradiction(sibling_parent_mismatch) :- siblings(X,Y), parent(X,Y).                
contradiction(sibling_grandparent_mismatch) :- siblings(X,Y), grandparent(X,Y).      
contradiction(sibling_uncle_mismatch) :- siblings(X,Y), uncle(X,Y).                  
contradiction(sibling_aunt_mismatch) :- siblings(X,Y), aunt(X,Y).                   


contradiction(child_grandparent_mismatch) :- child(X,Y), grandparent(Y,X).         
contradiction(child_uncle_mismatch) :- child(X,Y), uncle(Y,X).                       
contradiction(child_aunt_mismatch) :- child(X,Y), aunt(Y,X).                         

contradiction(child_parent_mismatch) :- child(X,Y), parent(X,Y).                    
contradiction(child_grandparent_mismatch) :- child(X,Y), grandparent(X,Y).     
contradiction(child_uncle_mismatch) :- child(X,Y), uncle(X,Y).                       
contradiction(child_aunt_mismatch) :- child(X,Y), aunt(X,Y).                        

contradiction(parent_grandparent_mismatch) :- parent(X,Y), grandparent(Y,X).       
contradiction(parent_uncle_mismatch) :- parent(X,Y), uncle(Y,X).                  
contradiction(parent_aunt_mismatch) :- parent(X,Y), aunt(Y,X).                  

contradiction(parent_grandparent_mismatch) :- parent(X,Y), grandparent(X,Y).        
contradiction(parent_uncle_mismatch) :- parent(X,Y), uncle(X,Y).               
contradiction(parent_aunt_mismatch) :- parent(X,Y), aunt(X,Y).                     

contradiction(grandparent_uncle_mismatch) :- grandparent(X,Y), uncle(Y,X).        
contradiction(grandparent_aunt_mismatch) :- grandparent(X,Y), aunt(Y,X).            

contradiction(grandparent_uncle_mismatch) :- grandparent(X,Y), uncle(X,Y).       
contradiction(grandparent_aunt_mismatch) :- grandparent(X,Y), aunt(X,Y).            

contradiction(uncle_aunt_mismatch) :- uncle(X,Y), aunt(Y,X).                       
contradiction(aunt_uncle_mismatch) :- aunt(Y,X), uncle(Y,X).                       

contradiction(uncle_aunt_mismatch) :- uncle(X,Y), aunt(X,Y).                    
contradiction(aunt_uncle_mismatch) :- aunt(Y,X), uncle(X,Y).                       

contradiction(too_many_parents) :- child(X, P1), child(X, P2), child(X, P3),P1 \= P2, P2 \= P3, P1 \= P3.

contradiction(too_many_grandmothers) :- grandmother(P1, X), grandmother(P2, X), grandmother(P3, X),P1 \= P2, P2 \= P3, P1 \= P3.
contradiction(too_many_grandfathers) :- grandfather(P1, X), grandfather(P2, X), grandfather(P3, X),P1 \= P2, P2 \= P3, P1 \= P3.