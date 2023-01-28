Given a positive integer number N. The task is to generate all the binary strings of N bits. These binary strings should be in ascending order.

Examples: 
 

Input: 2

Output:

0 0

0 1

1 0

1 1

Input: 3

Output:

0 0 0

0 0 1

0 1 0

0 1 1

1 0 0

1 0 1

1 1 0

1 1 1
 

Approach: The idea is to try every permutation. For every position, there are 2 options, either ‘0’ or ‘1’. Backtracking is used in this approach to try every possibility/permutation. 
