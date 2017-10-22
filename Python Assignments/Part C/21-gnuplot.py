##########################################################################
#
# Draw a 2-D plot for student registration number and the marks secured using gnuplot 
#
##########################################################################


import Gnuplot

# create lists to store student marks and regno
student_reg=[]
student_marks=[]


# get the register numbers and marks of the students
n = int(input("Enter number of students: "))
for i in range(0,n):
	reg = int(input("Enter RegNo: "))
	student_reg.append(reg)
	marks=int(input("Enter marks: "))
	student_marks.append(marks)

# plot students regno. and students marks
gplt = Gnuplot.Gnuplot(persist=1)
gplt.title("RegNo. V/S Marks")
gplt.xlabel("Student RegNo--->")
gplt.ylabel("Student Marks--->")
d=Gnuplot.Data(student_reg,student_marks,with_="line")

gplt.plot(d)
