:- dynamic male/1.
:- dynamic female/1.
:- dynamic parent/2.
:- dynamic child/2.
:- dynamic grandchild/2.
:- dynamic siblings/2.
:- dynamic uncle/2.
:- dynamic aunt/2.
:- dynamic cousin/2.
:- dynamic relative/2.
:- dynamic son/2.
:- dynamic grandmother/2.
:- dynamic grandfather/2.
:- dynamic daughter/2.
:- dynamic brother/2.
:- dynamic mother/2.
:- dynamic father/2.
:- dynamic children_of/4.
:- dynamic parents_of/3.

% parents
mother(X,Y) :- parent(X,Y), female(X), X \= Y.
father(X,Y) :- parent(X,Y), male(X), X \= Y.

% X and Y are the parents of Z
parents_of(X,Y,Z) :- child(Z,X), child(Z,Y), X \= Y.

% X Y and Z are the children of A
children_of(X,Y,Z,A) :- child(X,A),child(Y,A),child(Z,A),
             X \= Y, X \= Z, Y \= Z.

% children
child(X,Y) :- parent(Y,X), X \= Y.
son(X,Y) :- child(X,Y), male(X), X \= Y.
daughter(X,Y) :- child(X,Y), female(X), X \= Y.


%  grandparents A is subbed to any value
grandfather(X,Y) :- male(X), parent(X,A), parent(A,Y).
grandmother(X,Y) :- female(X), parent(X,A), parent(A,Y).

% siblings
siblings(X,Y) :- child(X,P), child(Y,P), X \= Y.
brother(X,Y) :- siblings(X,Y), male(X), X \= Y.
sister(X,Y) :- siblings(X,Y), female(X), X\= Y.

% relatives
uncle(X,Y) :- brother(X,P), child(Y,P), X\=Y.
aunt(X,Y) :- sister(X,P), child(Y,P), X \= Y.

% relatives logic
relatives(X, Y) :-
     X \= Y,
     (
         parent(X, Y);
         parent(Y, X);
         siblings(X, Y);
         child(X, Y);
         child(Y, X);
         grandfather(X, Y);
         grandfather(Y, X);
         grandmother(X, Y);
         grandmother(Y, X);
         uncle(X, Y);
         uncle(Y, X);
         aunt(X, Y);
         aunt(Y, X)
     ).