#Task 1: Generating a histogram for binomial distribution
'''
Generate 1000 fair coin toss trials
Produce a histogram that records the number of heads
Use 20 bins
'''

#initialize an empty array
heads = [] 

#use a for loop to run the fair coin tosses
for i in range(1000):
	heads.append(np.random.binomial(500, 0.5))

#plot histogram
histogram = plt.hist(heads, bins = 20)
plt.show()
