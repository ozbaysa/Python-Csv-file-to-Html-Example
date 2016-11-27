#######################################################
### Please ignore the following lines of code.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do NOT need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################
print ("<!DOCTYPE html>")
print ("<html>")
print ("<head>")
print ("<title>")
print ("State's Sat Score at 2004")
print ("</title>")
print ("<meta charset='UTF-8'>")
print ("</head>")
print ("<body style= 'background-color: red;'>")
print ('<table style ="border: 3px solid black;border-collapse:collapse;margin-left: 350px;">')
for i in range (3,56):
    print ("<tr>")
    print ("<td>")
    print (contents[i][0])
    print ("</td>")
    print ("<td>")
    print (contents[i][1])
    print ("</td>")
    print ("<td>")
    print (contents[i][2])
    print ("</td>")
    print ("</tr>")
print ("</table>")
print ("<br>")
print ("State List")
print ("<ol>")
for i in range (4,56):
    all_2004 = contents[i][0]
    print ("<li>")
    print (all_2004)
    print ("</li>")
print ("</ol>")
print ("<br>")
print ("Sum Of All States' Mean SAT I Math score at 2004: ")
print ("<ol>")
for i in range (4,56):
    all_2004 = float(contents[i][2])
    print ("<li>")
    print (all_2004)
    print ("</li>")
print ("</ol>")
while float(contents[10][1]) == 504:
    print("It is not printing anything. Because Maine's Verbal score is 505 ")
print ("New York State Mean SAT I Verbal score at 2004")
print (contents[4][1])
print ("New York State Mean SAT I Math score at 2004: ")
print (contents[4][2])
print ("<br>")
print ("Sum of Connecticut State and New Jersey State Mean SAT I Verbal score at 2004")
Sum_of_Math_con_new = (float(contents[5][1]) + float(contents[7][2]))
print (Sum_of_Math_con_new)
print ("<br>")
print ("Multiplication of Indiana State Mean SAT I Verbal score at 2004 and Texas State Mean SAT I Verbal Score at 2004: ")
Mul_of_Ver_score_bet_Ind04_tex03 = (float(contents[20][1])) * ( float(contents[25][1]))
print (Mul_of_Ver_score_bet_Ind04_tex03)
print ("<br>")
print ("SAT is score baced a exam known all over the US. If somebody want to go US collage's with scolarship. You need to take SAT.And This Table shows us score by state.")
print ("</body>")
print ("</html>")
