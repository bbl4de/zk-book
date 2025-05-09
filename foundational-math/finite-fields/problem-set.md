In the problems below, use a finite field p of 21888242871839275222246405745257275088548364400416034343698204186575808495617. Beware that the galois library takes a while to initialize a GF object, galois.GF(p), of this size.

1. A dev creates an arithmetic circuit x * y * z === 0 and x + y + z === 0 with the intent of constraining all the signals to be zero. Find a counter example to this where the constraints are satisfied, but not all of x, y, and z are 0.
2. A dev creates a circuit with the polynomial x² + 2x + 3 === 11 and proves that 2 is a solution. What is the other solution? Hint: write the circuit as x² + 2x - 8 === 0 then factor the polynomial by hand to find the roots. Finally, compute the congruent element of the roots in the finite field to find the other solution.

### Ad.1 
The most obvious example is (1, p-1, 0). 

For $x * y * z$ we get $0$ because of $z$ value. For $x + y + z$ the solution also becomes $0$ because $1 + p - 1 = p$ which in a finite field gets modulo'd to $0$ ( $p % p = 0$)

### Ad.2
Knowing one solution it's very simple to factor: $x^2+2x-8=(x-2)(x+4)$

So we know the solutions are $2$ and $-4$. The congruent for $-4$ is just $p-4$, which is: $21888242871839275222246405745257275088548364400416034343698204186575808495613$.