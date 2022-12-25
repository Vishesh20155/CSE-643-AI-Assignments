startSearch:-
    write('----------------------------------------------------'), nl,
    write('              Welcome to Path Finder'), nl, 
    write('----------------------------------------------------'), nl, nl,

    write('Enter 1. for Depth First Search and 2. for Best First Search'), nl, read(Opt), nl,
    executeChoice(Opt).

executeChoice(1):-
    searchDFS.

executeChoice(2):-
    searchBFS.

executeChoice(_):-
    write('Invalid Choice!! Try Running the Program Again').

searchDFS:-
    nl, write('Enter the city names in single quotes: '), nl, nl,
    write('Enter the starting point: '), nl, read(Source),
    write('Enter the Ending Point: '), nl, read(Destination), nl,
    graphDFS(Source, Destination).
    % graphDFS('Bangalore', 'Bhubaneshwar').
    % graphDFS('Bangalore', 'Ahmedabad').
    % graphDFS('Ahmedabad', 'Agartala').

graphDFS(Src, Dest):-
    dfs(Src, Dest, 4, [], Cost, Path),
    write('The path is: '), nl,
    printPath(Path), nl, write('The total distance (cost) is: '), write(Cost), !.

dfs(Src, Src, _, CurrPath, Cost, [Src|CurrPath]):-Cost is 0.

dfs(Src, Dest, Depth, CurrPath, Cost, Path):-
    Depth>0,
    distance(Src, N, C),
    \+ member(N, CurrPath),
    D is Depth-1,
    dfs(N, Dest, D, [Src|CurrPath], Cost1, Path),
    Cost is Cost1+C.

searchBFS:-
    nl, write('Enter the city names in single quotes: '), nl, nl,
    write('Enter the starting point: '), nl, read(Source),
    write('Enter the Ending Point: '), nl, read(Destination), nl,
    heuristicDistance(Source, Destination, HueVal), 
    bestFirst(Source, Destination, [[Source, HueVal]], [], Cost, Path),
    % bestFirst('Ahmedabad', 'Ahmedabad', [['Ahmedabad', 0]], [], Cost, Path),
    % bestFirst('Agra', 'Hubli', [['Agra', 1342]], [], Cost, Path),
    % bestFirst('Ahmedabad', 'Bangalore', [['Ahmedabad', 1231]], [], Cost, Path),
    % bestFirst('Ahmedabad', 'Agra', [['Ahmedabad', 715]], [], Cost, Path),
    % bestFirst('Gwalior', 'Ludhiana', [['Gwalior', 568]], [], Cost, Path),

    write('The path is: '), nl, 
    printPath(Path), nl,
    write('The total distance (cost) is: '), writeln(Cost), !.

bestFirst(Src, Src, _, CurrPath, Cost, [Src|CurrPath]):- Cost is 0.

bestFirst(Src, Dest,  [_|T], CurrPath, Cost, Path):-
    findall([Node, HeuDist], (distance(Src, Node, _), heuristicDistance(Node, Dest, HeuDist)), L),
    map_list_to_pairs(getHeuDist, L, Pairs),
    map_list_to_pairs(getHeuDist, T, Pairs1),
    append(Pairs, Pairs1, Pairs2),
    keysort(Pairs2, Sorted), pairs_values(Sorted, S), 
    [H1|_] = S,
    [H2|_] = H1,
    % writeln(S), nl,
    bestFirst(H2, Dest, S, [Src|CurrPath], Cost1, Path),
    distance(Src, H2, C),
    Cost is Cost1+C.
    % writeln(H1), nl, writeln(H2), nl.

getHeuDist([_, X|_], N):-
    N is X.


printPath([H]):-
    write(H), !.

printPath([H|T]):-
    printPath(T),
    write('->'), write(H).
