#Thomas 
#Cramer's Method
#December 18, 2014

row_Num = 1 #It asks for each row so to keep track it has a variable that is incremented after every row that gets entered by the user. 

matrixA=[]; matrixB=[] #Matrix A contains x and y coefficients and matrixB contains the solution constants.

for i in range(2): #The user puts in each line of Matrix A separately
	row = input("A Matrix - row # " + str(row_Num) + " (Deliminate by space): ")
	row_Num += 1 #This will print row1, row 2, row 3, etc. as the user inputs rows
	row = row.split() #Splits the one row into a list 
	matrixA.append(row) #Which is appended to the matrix list
	
print() #Skip a space for formatting 
row_Num = 1 #row number goes back to one for the second matrix

for i in range(2): #Then the user adds the solution constants
	row = input("B Matrix - row # {} (Deliminate by space): ".format(row_Num)) #I don't like concatenating, I never remember the str() so I used .format method
	row_Num += 1
	row = row.split()
	matrixB.append(row) 

for i in range(len(matrixA)): #Each number in each row (which is stored as a list) in each Matrix (which are also lists) must be converted to an integer
	for k in range(len(matrixA[i])): #see below
		matrixA[i][k] = float(matrixA[i][k])
for i in range(len(matrixB)): #For each row (list) in the Matrix
	for k in range(len(matrixB[i])): #For each number in the row
		matrixB[i][k] = float(matrixB[i][k]) #make that number an integer
	
#This calls elements of the Matrices, where it indexes a row of the Matrix then the element of that row. 
D = matrixA[0][0] * matrixA[1][1] - matrixA[0][1] * matrixA[1][0] #First the diagnals in MatrixA

Dx = matrixB[0][0] * matrixA[1][1] - matrixA[0][1] * matrixB[1][0] #Then it replaces the x-coordinates with the solution constants from B

Dy = matrixA[0][0] * matrixB[1][0] - matrixA[1][0] * matrixB[0][0]#Then it replaces the y-coordinates with the solution constants from B
	
x = Dx/D #Division for coordinates
y = Dy/D
print("\nx-coordinate: {}".format(x))
print("y-coordinate: {}".format(y)) #PRINTING RESULTS
print("Solution: ({}, {})".format(x, y)) #I really do not like concatenating

#END
