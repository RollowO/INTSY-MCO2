% facts

% gender
male(X).
female(X).

% parents
parent(X,Y).
mother(X,Y) :- parent(X,Y), female(X), X \= Y.
father(X,Y) :- parent(X,Y), male(X), X \= Y.

% X and Y are the parents of Z
parents_of(X,Y,Z) :- child(Z,X), child(Z,Y), X \= Y

% X Y and Z are the children of A
children_of(X,Y,Z,A) :- child(X,A),child(Y,A),child(Z,A), 
            X \= Y, X \= Z, Y \= Z.

% children
child(X,Y) :- parent(Y,X), X \= Y.
son(X,Y) :- child(X,Y), male(X), X \= Y.
daughter(X,Y) :- child(X,Y), daughter(X), X \= Y.


%  grandparents A is subbed to any value
grandfather(X,Y) :- male(X), parent(X,A), parent(A,Y). 
grandmother(X,Y) :- female(X), parent(X,A), parent(A,Y).

% siblings

siblings(X,Y) :- child(X,P), child(Y,P), X \= Y.
brother(X,Y) :- siblings(X,Y), male(X), X \= Y.
sister(X,Y) :- siblings(X,Y), female(X), X\= Y.

% relatives
uncle(X,Y) :- brother(X,P), child(Y,P), X\=Y
aunt(X,Y) :- sister(X,P), child(Y,P), X\=Y

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
