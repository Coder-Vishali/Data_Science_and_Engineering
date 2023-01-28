# Shakuntala challenge

# Problem Statement 

In the movie about the famous Indian mathematician Shakuntala Devi, she is seen solving difficult 
mathematical questions in a matter of seconds. Her techniques for multiplying large numbers were 
not standard methods and she was also able to beat the fastest computers at that time. 
Assuming you were one of the computer programmers of that era and had the power of superior 
algorithms at your disposal, you were given the task to design a system that did not follow the 
standard multiplication algorithm that took n2 operations but was better and faster than that. 

Among the various options available, one method is to split each number x and y into two parts:

x = 10n/2 * a + b, y = 10n/2 * c + d. 

Then, 
x * y = 10n (a*c) +10n/2 (a*d + b*c) + b*d. 


# Requirements:

1. Identify which design strategy is employed here and give a brief explanation about the same.
2. Use recurrence relations to find the number of multiplication operations required using this 
approach. Briefly explain the steps involved.
3. Analyse the time complexity of your algorithm.
4. Implement the above problem statement using Python 3.7. 

# Sample Input:

Input of two numbers A and B should be taken in as user input from input.txt. 

Number 1: 223245

Number 2: 123456

Note that the input/output data shown here is only for understanding and testing, the actual file used 
for evaluation will be different.

# Sample Output:

---------------------------

1st number, x: 221234

2nd number, y: 123456

Intermediate Values of A, B after partition:

x: 221234 a : 221 b : 234

y: 123456 c : 123 d : 456

---------------------------

1st number, x: 221

2nd number, y: 123

Intermediate Values of A, B after partition:

x: 221 a : 22 b : 1

y: 123 c : 12 d : 3

---------------------------

1st number, x: 22

2nd number, y: 12

Intermediate Values of A, B after partition:

x: 22 a : 2 b : 2

y: 12 c : 1 d : 2

Intermediate Product: 22 x 12 = 264

---------------------------

1st number, x: 23

2nd number, y: 15

Intermediate Values of A, B after partition:

x: 23 a : 2 b : 3

y: 15 c : 1 d : 5

Intermediate Product: 23 x 15 = 345

---------------------------

Intermediate Product: 221 x 123 = 27183

---------------------------

1st number, x: 234

2nd number, y: 456

Intermediate Values of A, B after partition:

x: 234 a : 23 b : 4

y: 456 c : 45 d : 6

---------------------------

1st number, x: 23

2nd number, y: 45

Intermediate Values of A, B after partition:

x: 23 a : 2 b : 3

y: 45 c : 4 d : 5

Intermediate Product: 23 x 45 = 1035

---------------------------

1st number, x: 27

2nd number, y: 51

Intermediate Values of A, B after partition:

x: 27 a : 2 b : 7

y: 51 c : 5 d : 1

Intermediate Product: 27 x 51 = 1377

---------------------------

Intermediate Product: 234 x 456 = 106704

---------------------------

1st number, x: 455

2nd number, y: 579

Intermediate Values of A, B after partition:

x: 455 a : 45 b : 5

y: 579 c : 57 d : 9

---------------------------

1st number, x: 45

2nd number, y: 57

Intermediate Values of A, B after partition:

x: 45 a : 4 b : 5

y: 57 c : 5 d : 7

Intermediate Product: 45 x 57 = 2565

---------------------------

1st number, x: 50

2nd number, y: 66

Intermediate Values of A, B after partition:

x: 50 a : 5 b : 0

y: 66 c : 6 d : 6

Intermediate Product: 50 x 66 = 3300

---------------------------

Intermediate Product: 455 x 579 = 263445

---------------------------

Intermediate Product: 221234 x 123456 = 27312664704

---------------------------

Result:> 221234 x 123456 = 27312664704
