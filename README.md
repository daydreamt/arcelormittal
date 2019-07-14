This code is my contribution to our submission to the ArcelorMittal hackathon held in Zaventem, Belgium https://challenge.arcelormittal.com/ on the 22nd of September 2018.

You can see the presentation [here](SuperVisor.pdf)


# Data
## Getting the data
### Youtube queries to get data (max of 50 videos):
1. steel factory accident
2. steel mill accident
3. casting line accident # Also has fishing videos, and Mr Bean at the doctor
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


# Image classifiers on this data:
CLASSIFIER 1: 	PROBLEM / NO PROBLEM

	ENH: 1.THE WHOLE VIDEOS WE HAVE FROM 0:00 ARE OF 'PROBLEM'  THE WHOLE VIDEOS WE HAVE FROM -1 ARE OF 'NO PROBLEM'
	resnet 18: 0.988 accuracy on validation set
	
CLASSIFIER 2:

	PROBLEM / NO PROBLEM 10 seconds ahead.

# Text classifiers:
- Currently show and tell applied on every frame.

- we also have word embeddings from the documents

- obviously we also have the embeddings from the images

- not matching currently

# HOW TO USE THE PROVIDED TEXTS?
- We could can get multimodal embeddings e.g. with  https://github.com/linxd5/VSE_Pytorch Then all we would have to do to match embeddings to scenarios, is for every frame to apply this model, and find the closest safety protocol.

- We have currently difficulty extracting the instructions from the documents nicely

- The best way to solve this problem, is to align frames to sentences, like in machine translation

- then, we can find for every frame the closest scenario steps (k-d tree?)

- and detect *any* deviation from standard protocol.


