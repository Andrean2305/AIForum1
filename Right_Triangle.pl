% forum6/3: Ensures that the sum of three angles A1, A2, and A3 is 180 degrees,
% at least one of them is 90 degrees, and all angles are greater than 0.

forum6(A1, A2, A3) :-
    % Check if the sum of angles is 180 degrees
    (A1 + A2 + A3 =:= 180),
    
    % Ensure at least one angle is 90 degrees
    (A1 =:= 90 ; A2 =:= 90 ; A3 =:= 90),
    
    % Ensure that all angles are greater than 0
    A1 > 0,
    A2 > 0,
    A3 > 0.
