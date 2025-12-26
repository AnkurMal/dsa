## Lagrange's four-square theorem

Lagrange's four-square theorem, also known as Bachet's conjecture, states that every nonnegative integer can be represented as a sum of four non-negative integer squares. That is, the squares form an additive basis of order four:  

$$
p = a^2 + b^2 + c^2 + d^2
$$  

where the four numbers $a, b, c, d$ are integers. For illustration, 3, 31, and 310 can be represented as the sum of four squares as follows:  

$$
\begin{aligned}
3 &= 1^2 + 1^2 + 1^2 + 0^2 \\
31 &= 5^2 + 2^2 + 1^2 + 1^2 \\
310 &= 17^2 + 4^2 + 2^2 + 1^2 \\
    &= 16^2 + 7^2 + 2^2 + 1^2 \\
    &= 15^2 + 9^2 + 2^2 + 0^2 \\
    &= 12^2 + 11^2 + 6^2 + 3^2 \\
\end{aligned}
$$

Therefore, we can deduce that any positive number can be expressed as sum of at-most 4 square numbers.

### Case 1:

    If number is a perfect square => minimum number of squares needed = 1 
    Example : 1, 4, 9, etc.

### Case 2:

    If the number is the sum of 2 square numbers => minimum number of squares needed = 2 
    Example : 2, 5, 18, etc. 

### Case 3:

    If the number is not of the form 4k x (8m + 7) such that k, m ∈ W => minimum number of squares needed = 3
    Example : 6, 11, 12 etc.

### Case 4:

    If the number is of the form 4k x (8m + 7) such that k, m ∈ W => minimum number of squares needed = 4
    Example : 7, 15, 23 etc.