gpa =['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'E']
score = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2, 1.7, 1, 0.8]

credits =0
totalCredit = 0 

while True:
    inputGPA = eval(input("your gpa is:"))
    if inputGPA in gpa:
        c = eval(input("this course credit is:"))
        totalCredit += c*score[gpa.index(inputGPA)]
        credits += c
        print('total cradit:', credits, '/average:', totalCredit/credits)
    else:
        break
