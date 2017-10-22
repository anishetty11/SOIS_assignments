###############################################################
#
# Program to plot the marks WRT to register number using matplotlib
#
###############################################################
import matplotlib.pyplot as plt

#dictionary containing reg no as keys and marks as value
marks={100:44,101:44,102:43,103:12,104:21}
#print (marks)

#create the list containing all the register numbers
reg=list(marks.keys())
reg.sort()

# add the marks of each reg nos in "scores"
score=[]
for x in reg:
	score.append(marks[x])

# plot the graph with reg no in x axis and score in y axis
plt.plot(reg,score)
plt.show()
