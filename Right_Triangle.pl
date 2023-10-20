forum6(A1, A2, A3) :-
    %check sum
    A1 + A2 + A3 =:= 180,
    %1 have to be 90
    (A1 =:= 90 ; A2 =:= 90 ; A3 =:= 90).