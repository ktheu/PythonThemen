include "globals.mzn";
int: nSpot;
set of int: SPOT = 1..nSpot;

int: k;
set of int: CLUSTER = 1..k;

float: maxSep;
array[SPOT, SPOT] of float: dist;

array[1..nSpot] of var CLUSTER: x;  % clustering decisions

constraint forall(i,j in SPOT where x[i] = x[j])(dist[i, j] <= maxSep); % intra-cluster

    
constraint value_precede_chain(CLUSTER, x);

constraint global_cardinality_low_up_closed(x,
  [i | i in CLUSTER], [1 | i in CLUSTER],
  [nSpot-k+1 | i in CLUSTER]);

% constraint forall (i in 1..k-1)
%     (min([j | j in SPOT where x[j] = i]) < min([j | j in SPOT where x[j] = i+1]));

float: maxdist = max([dist[i, j] | i, j in SPOT]); % auxiliary variable
var float :obj = min(i, j in SPOT where i < j)(if x[i] = x[j] then maxdist else dist[i, j] endif); % inter-cluster
solve maximize obj;

output[show(x), ", obj = ", show(obj)];
