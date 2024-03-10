# Regular-Proportional-STAR-Voting-without-1on1-runoffs
This is a Python program that let's you simulate proportional STAR Voting / Allocated Score Voting as defined by the Equal Vote Coalition. There are no Automatic 1on1 Runoffs after each round. The highest scoring candidate after each round wins a seat.

Use: Just copy and paste the code into a Python Interpreter, run, and the program will ask you how many candidates are running, what their names are, how many seats can be won, and what the ballot scores are. You can paste the code and run it here: https://www.programiz.com/python-programming/online-compiler/

Output: The program will output the scores of the candidates each round, and who the winners are.

Credits: I used the algorithm used for regular Proportional STAR / Allocated Score from https://electowiki.org/wiki/Allocated_Score for the regular allocated score part. I then added an algorithm to count runoff votes.


 
Tennessee Example https://en.wikipedia.org/wiki/STAR_voting#Example
       
        |            |   City Choice |              |              |               |             |         |
        |------------|---------------|--------------|--------------|---------------|-------------|---------|
        | Voter from |               | Memphis      | Nashville    | Chattanooga   | Knoxville   |  Total  |
        |------------|---------------|--------------|--------------|---------------|-------------|---------|
        |            |   Memphis     | 210 (42 × 5) | 0 (26 × 0)   | 0 (15 × 0)    | 0 (17 × 0)  |  210    | 
        |------------|---------------|--------------|--------------|---------------|-------------|---------|
        |            |   Nashville   | 84 (42 × 2)  | 130 (26 × 5) | 45 (15 × 3)   | 34 (17 × 2) |  293    |
        |------------|---------------|--------------|--------------|---------------|-------------|---------|
        |            |   Chattanooga | 42 (42 × 1)  | 52 (26 × 2)  | 75 (15 × 5)   | 68 (17 × 4) |  237    |
        |------------|---------------|--------------|--------------|---------------|-------------|---------|
        |            |   Knoxville   | 0 (42 × 0)   | 26 (26 × 1)  | 45 (15 × 3)   | 85 (17 × 5) |  156    |
  
Demo with Droop Quota:

Enter the number of candidates: 4

Enter the name of candidate 1: Memphis

Enter the name of candidate 2: Nashville

Enter the name of candidate 3: Chattanooga

Enter the name of candidate 4: Knoxville

Enter the number of seats: 3

Enter all the scores separated by space (for all voters, each group represents one voter's ballot with no spaces within each ballot, but spaces separating each separate individual ballot, e.g., 43250 21532 23145): 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 5210 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0521 0353 0353 0353 0353 0353 0353 0353 0353 0353 0353 0353 0353 0353 0353 0353 0245 0245 0245 0245 0245 0245 0245 0245 0245 0245 0245 0245 0245 0245 0245 0245 0245

Round 1 - Scores of the candidates:
Nashville: 293
Chattanooga: 237
Memphis: 210
Knoxville: 156

Round 2 - Scores of the candidates:
Memphis: 210
Chattanooga: 185
Knoxville: 130

Round 3 - Scores of the candidates:
Chattanooga: 159
Knoxville: 130

Winners: ['Nashville', 'Memphis', 'Chattanooga']
