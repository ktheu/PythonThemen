from minizinc import Instance, Model, Solver

gecode = Solver.lookup("gecode")

trivial = Model()
trivial.add_string('''
% ----- Parameters -----
int: n=2;
array[1..n] of int: sp = [1, 0];
array[1..n] of int: ze = [0, 1];
array[1..2*n-1] of int: d1 = [0, 1, 0];
array[1..2*n-1] of int: d2 = [1, 0, 0];
array[1..n] of array[int] of int: spalten = [[0, 2], [1, 3]];
array[1..n] of array[int] of int: zeilen = [[0, 1], [2, 3]];
array[1..2*n-1] of array[int] of int: diagonals1 = [[0], [1, 2], [3]];
array[1..2*n-1] of array[int] of int: diagonals2 = [[2], [3, 0], [1]];

% ----- Decision variables -----
array[0..n*n-1] of var bool: x;

% ----- Constraints -----
% Spalten
constraint
    forall(i in 1..n)(
        sum(j in 1..n)( x[spalten[i][j]] ) = sp[i]
    );

% Zeilen
constraint
    forall(i in 1..n)(
        sum(j in 1..n)( x[zeilen[i][j]] ) = ze[i]
    );

% Diagonalen1 
constraint
    forall(i in 1..2*n-1)(
        sum(j in index_set(diagonals1[i]))( x[diagonals1[i][j]] ) = d1[i]
    );

% Diagonalen2
constraint
    forall(i in 1..2*n-1)(
        sum(j in index_set(diagonals2[i]))( x[diagonals2[i][j]] ) = d2[i]
    );

% ----- Solve -----
solve satisfy;
'''
)
instance = Instance(gecode, trivial)


# Find and print all intermediate solutions
result = instance.solve(intermediate_solutions=True)
for i in range(len(result)):
    print(result(i), "x"])
 