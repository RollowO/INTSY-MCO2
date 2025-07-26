:- dynamic father/2, mother/2, parent/2, male/1, female/1, ancestor/2.
%rules
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

child(X, Y) :- parent(Y, X).
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

brother(X, Y) :-
    sibling(X, Y),
    male(X).

sister(X, Y) :-
    sibling(X, Y),
    female(X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandchild(X, Y) :-
    grandparent(Y, X).

grandfather(X, Y) :- father(X, Z), parent(Z, Y).
grandmother(X, Y) :- mother(X, Z), parent(Z, Y).

uncle(X, Y) :-
    male(X),
    sibling(X, Z),
    parent(Z, Y).

aunt(X, Y) :-
    female(X),
    sibling(X, Z),
    parent(Z, Y).

cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).

daughter(X, Y) :-
    child(X, Y),
    female(X).

son(X, Y) :-
    child(X, Y),
    male(X).

%relatives
relatives(X, Y) :- sibling(X, Y).
relatives(X, Y) :- parent(X, Y).
relatives(X, Y) :- parent(Y, X).
relatives(X, Y) :- grandparent(X, Y).
relatives(X, Y) :- grandparent(Y, X).
relatives(X, Y) :- uncle(X, Y).
relatives(X, Y) :- uncle(Y, X).
relatives(X, Y) :- cousin(X, Y).
relatives(X, Y) :- cousin(Y, X).

%Recursive relations
% Depth-limited ancestor
ancestor(X, Y, 0) :- parent(X, Y).
ancestor(X, Y, N) :-
    N > 0,
    parent(X, Z),
    N1 is N - 1,
    ancestor(Z, Y, N1).

