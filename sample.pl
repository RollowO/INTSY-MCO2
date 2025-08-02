% Facts: male(person), female(person), parent_of(parent, child)

% Rules for relationships

% X and Y are siblings
siblings(X, Y) :-
  parent_of(P, X),
  parent_of(P, Y),
  X \= Y.

% X is a son of Y
son(X, Y) :-
  male(X),
  parent_of(Y, X).

% X is a sister of Y
sister(X, Y) :-
  female(X),
  parent_of(P, X),
  parent_of(P, Y),
  X \= Y.

% X is a grandmother of Y
grandmother(X, Y) :-
  female(X),
  parent_of(X, P),
  parent_of(P, Y).

% X is a grandfather of Y
grandfather(X, Y) :-
  male(X),
  parent_of(X, P),
  parent_of(P, Y).

% X is a child of Y
child(X, Y) :-
  parent_of(Y, X).

% X is a daughter of Y
daughter(X, Y) :-
  female(X),
  parent_of(Y, X).

% X is a brother of Y
brother(X, Y) :-
  male(X),
  parent_of(P, X),
  parent_of(P, Y),
  X \= Y.

% X is an uncle of Y
uncle(X, Y) :-
  male(X),
  parent_of(P, Y),
  brother(X, P).

% X is an aunt of Y
aunt(X, Y) :-
  female(X),
  parent_of(P, Y),
  sister(X, P).

% X is the mother of Y
mother(X, Y) :-
  female(X),
  parent_of(X, Y).

% X is the father of Y
father(X, Y) :-
  male(X),
  parent_of(X, Y).

% X and Y are the parents of Z
parents(X, Y, Z) :-
  parent_of(X, Z),
  parent_of(Y, Z).

% X, Y and Z are children of A
children(X, Y, Z, A) :-
  parent_of(A, X),
  parent_of(A, Y),
  parent_of(A, Z).

% X and Y are relatives
relatives(X, Y) :-
  parent_of(X, Y).
relatives(X, Y) :-
  parent_of(Y, X).
relatives(X, Y) :-
  siblings(X, Y).
relatives(X, Y) :-
  parent_of(P, X),
  parent_of(P, Y),
  X \= Y.
relatives(X, Y) :-
    parent_of(P,X),
    relatives(P,Y).
relatives(X, Y) :-
    parent_of(P,Y),
    relatives(P,X).
