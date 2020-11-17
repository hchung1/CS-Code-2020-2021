# Testing Library
import unittest
# Library to Verify Answers
import numpy as np

class math_class():
    def matmul(self, matrix1, matrix2): # 2D Matrix Multiplication
        if len(matrix1[0]) == len(matrix2):
            temp=[]
            matrix2=self.transpose(matrix2)
            counter=0
            for i in matrix1:
                temp.append([])
                for j in matrix2:
                    temp[counter].append(sum([i[x]*j[x] for x in range(len(i))]))
                counter +=1
            return temp
        else:
            print ("Error: Dimension mismatch, K-size is different. (n?,k),(k,m?)->(n?,m?)")
    def transpose(self, data): # 2D Transpose
        try:
            temp = []
            for i in range(len(data[0])):
                temp.append([])
                for j in range(len(data)):
                    temp[i].append(data[j][i])
            return temp
        except:
            print ("Error: %s is not a 2D array." % str(data))
            return data

# Variables
test1 = [[1,2,3]] # Test 1, 1x3 Vector
test2 = [[1,2,3],[3,4,5]] # Test 2, 2x3 Matrix
test_const = [[1,2,3,5],[4,5,6,3],[7,8,9,1]] # Test Constant, 3x4 Matrix

# Call Class
tester = math_class()

# Run Matrix Multiplication
result1 = tester.matmul(test1,test_const) # Result 1, 1x4 Matrix
result2 = tester.matmul(test2,test_const) # Result 2, 2x4 Matrix

# Create Checking Model (Numpy)
check_const = np.array(test_const) # Check Constant, 3x4 Matrix
check1 = np.matmul(np.array(test1),check_const) # Check 1, 1x4 Matrix
check2 = np.matmul(np.array(test2),check_const) # Check 2, 2x4 Matrix


# Output Result and Check
print ("My Result")
print (result1)
print ("\nNumpy Result")
print (check1)
print ("\n\nMy Result")
print (result2)
print ("\nNumpy Result")
print (check2)
