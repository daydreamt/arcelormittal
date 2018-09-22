# arcelormittal


# Data
## Getting the data
### Youtube queries to get data (max 50 videos):
1. steel factory accident
2. steel mill accident
3. casting line accident # Also has some fishing videos, and Mr Bean at the doctor
4. hot strip mill accident #10
5. continuous annealing line accident #10
6. jet vapor deposition accident #10
7. hot dip galvanising line accident #10

## Labeling:
$ head accident_times.txt
3EdQq5iAGYs.mp4 3:14
3LQ7ANm3lqA.mp4 0:00
MxGcX-spcHo.mp4 -1


1. The moment of accident: e.g. 00:42
2. -1: no accident occurs, normal operation
3. none: no accident occurs, random footage
4. 0:00: accident has already occured
5. many occur








# IMAGE CLASSIFIERS ON THIS DATA:
CLASSIFIER 1:
	PROBLEM / NO PROBLEM
	FOR THIS: ALL FRAMES WE HAVE RIGHT NOW
	PLUS: THE WHOLE VIDEOS WE HAVE FROM 0:00 ARE OF 'PROBLEM'
	PLUS: THE WHOLE VIDEOS WE HAVE FROM -1 ARE OF 'NO PROBLEM'
	
	THIS IS: TRANSFER LEARNING CLASSIFIER

CLASSIFIER 2:
	PROBLEM IN N FRAMES/ NO PROBLEM
	DATA: SAME AS ABOVE
	BUT ALSO SEQUENCES

Me/Nozomi/Irzam, but maybe no hardware unless jupyter notebook

# CROSS MODAL MATCHING?
The biggest problem is how to match the seq 1 to seq 2
	Well, if we could match the individual components to each other
	then it becomes only a search problem

	the data structure you want is a kind of tree
