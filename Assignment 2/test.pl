:- use_module(library(csv)).


start:-
    write('Hello 1'), nl,
    retractall(distance(_, _, _)),
    write('Hello 2'), nl,
    readDistances,
    write('Hello 3'), nl.

readDistances:-
    csv_read_file('roaddistance.csv', Rows, [functor(table)]),
    Rows = [H|T],
    % T = [H1|_],
    % write(H), nl, write(H1), nl.
    forall(member(R, T), createDistanceFact(H, R)).

createDistanceFact(HeaderRow, TableRow):- 
    % write(TableRow), nl,
    arg(1, TableRow, From), 
    functor(HeaderRow, _, NoOfCols),
    findall(I, between(2, NoOfCols, I), Indices),   % Iterating over all columns  
    forall(member(D, Indices), addFact(From, D, HeaderRow, TableRow)).

addFact(From, ToIndex, HeaderRow, CurrentRow):-
    % write(From), write('-'),
    arg(ToIndex, HeaderRow, To),
    arg(ToIndex, CurrentRow, Dist),
    % write(To), write(': '), write(Dist), nl,
    assertAsFact(From, To, Dist).

assertAsFact(From, From, _).
assertAsFact(From, To, Dist):-
    (retract(distance(From, To, Dist)), !); assert(distance(From, To, Dist)),
    (retract(distance(To, From, Dist)), !); assert(distance(To, From, Dist)).
    