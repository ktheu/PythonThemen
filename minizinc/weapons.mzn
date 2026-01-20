enum WEAPON = {AXE, SWORD, PIKE, SPEAR, CLUB};
enum RESOURCE = {IRON, WOOD, SMITH, CARPENTER};

array[WEAPON] of float: strength = [11.0, 18.0, 15.0, 17.0, 11.0];
array[RESOURCE] of float: capacity = [5000, 7500, 4000, 3000]; 
array[WEAPON,RESOURCE] of float: consumption = [| 1.5, 1.0, 1.0, 1.0 
                                                | 2.0, 0.0, 2.0, 0.0
                                                | 1.5, 0.5, 1.0, 1.0 
                                                | 0.5, 1.0, 0.9, 1.5
                                                | 0.1, 2.5, 0.1, 2.5 |];
% decision variables
array[WEAPON] of var int: amt;       
 
% constraints
constraint forall(w in WEAPON) (amt[w] >= 0);
constraint forall (r in RESOURCE)(
      sum (w in WEAPON)(consumption[w, r] * amt[w]) <= capacity[r]
); 

% objective
solve maximize sum(w in WEAPON)(strength[w]*amt[w]);

% output
output [ "\(w): \(amt[w])\n" | w in WEAPON ]++["STRENGTH: \(sum(w in WEAPON)(strength[w]*amt[w]))"];